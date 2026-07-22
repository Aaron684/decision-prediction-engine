from dataclasses import dataclass
from typing import Any


@dataclass
class FeatureMetadata:

    name: str

    data_type: str


@dataclass
class TrainingDataset:

    X: list[list[float]]

    y: list[float]

    feature_names: list[str]

    feature_types: list[str]

    target_name: str

    target_type: str


@dataclass
class TrainedModel:

    model: Any

    model_id: str

    model_name: str

    features: list[FeatureMetadata]

    target_name: str

    target_type: str

    observation_count: int


@dataclass
class ModelEvaluation:

    model_id: str

    model_name: str

    estimator: Any

    primary_score: float

    secondary_metrics: dict[str, float]

    cv_strategy: str

    failed: bool = False

    error_message: str | None = None


@dataclass
class ModelLeaderboard:

    evaluations: list[ModelEvaluation]

    @property
    def successful(self):
        return [
            e for e in self.evaluations
            if not e.failed
        ]

    @property
    def failed(self):
        return [
            e for e in self.evaluations
            if e.failed
        ]