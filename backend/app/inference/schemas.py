from dataclasses import dataclass
from typing import Any

from app.training.explainability.schemas import (
    PredictionExplanation,
)

@dataclass
class PredictionRequest:
    values: dict[str, Any]


@dataclass
class PredictionResult:
    prediction: Any


@dataclass
class PredictionRequest:

    values: dict[str, Any]


@dataclass
class PredictionResult:

    prediction: Any

    explanation: PredictionExplanation