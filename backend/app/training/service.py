from sqlalchemy.orm import Session

from app.repositories.model_repository import ModelRepository

from app.training.pipeline import (
    build_training_dataset,
)

from app.training.comparison import (
    compare_models,
)

from app.training.trainer import (
    train_best_model,
)

from app.schemas.training import (
    TrainingResult,
)


class TrainingService:

    def __init__(
        self,
        repository: ModelRepository,
    ):
        self.repository = repository

    def train_category(
    self,
    db: Session,
    category_id: int,
) -> TrainingResult:

        dataset = build_training_dataset(
            db=db,
            category_id=category_id,
        )

        leaderboard = compare_models(
            dataset,
        )

        trained_model = train_best_model(
            dataset,
            leaderboard,
        )

        winner = leaderboard.best()

        self.repository.save_model(
            db=db,
            category_id=category_id,
            trained_model=trained_model,
            primary_score=winner.primary_score,
        )

        return TrainingResult(
            model_name=winner.model_name,
            model_id=winner.model_id,
            observation_count=len(dataset.y),
            primary_score=winner.primary_score,
        )