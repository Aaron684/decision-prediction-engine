from app.training.leaderboard import ModelLeaderboard
from app.training.model_factory import create_registered_model
from app.training.schemas import (
    TrainingDataset,
    TrainedModel,
)


def train_best_model(
    dataset: TrainingDataset,
    leaderboard: ModelLeaderboard,
) -> TrainedModel:

    winner = leaderboard.best()

    estimator = create_registered_model(
        dataset.target_type,
        winner.model_id,
    )

    estimator.fit(
        dataset.X,
        dataset.y,
    )

    return TrainedModel(
        model=estimator,
        model_name=winner.model_name,
        feature_names=dataset.feature_names,
        target_name=dataset.target_name,
        target_type=dataset.target_type,
        observation_count=len(dataset.y),
    )