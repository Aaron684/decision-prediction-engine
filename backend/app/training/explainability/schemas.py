from dataclasses import dataclass
from typing import Any


@dataclass
class FeatureContribution:

    feature_name: str

    feature_value: Any

    importance: float

    direction: str | None

@dataclass
class PredictionExplanation:

    method: str

    confidence: float | None

    feature_contributions: list[FeatureContribution]

@dataclass
class PredictionResult:

    prediction: Any

    explanation: PredictionExplanation