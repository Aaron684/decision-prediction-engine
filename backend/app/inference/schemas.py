from dataclasses import dataclass
from typing import Any


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