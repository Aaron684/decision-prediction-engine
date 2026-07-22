from app.training.leaderboard import ModelLeaderboard
from app.training.model_factory import create_registered_model
from app.training.schemas import (
    TrainingDataset,
    TrainedModel,
    FeatureMetadata
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

    features = [
        FeatureMetadata(
            name=name,
            data_type=data_type,
        )
        for name, data_type in zip(
            dataset.feature_names,
            dataset.feature_types,
        )
    ]


    return TrainedModel(
        model=estimator,
        model_id=winner.model_id,
        model_name=winner.model_name,
        features=features,
        target_name=dataset.target_name,
        target_type=dataset.target_type,
        observation_count=len(dataset.y),
    )