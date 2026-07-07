from dataclasses import dataclass


@dataclass
class TrainingDataset:
    X: list[list[float]]
    y: list[float]
    feature_names: list[str]
    target_name: str
    target_type: str