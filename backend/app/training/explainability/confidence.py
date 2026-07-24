from abc import ABC, abstractmethod

from app.training.schemas import TrainedModel

    
from app.training.explainability.utils import get_estimator


class BaseConfidenceProvider(ABC):

    @abstractmethod
    def supports(
        self,
        trained_model: TrainedModel,
    ) -> bool:
        raise NotImplementedError


    @abstractmethod
    def get_confidence(
        self,
        trained_model: TrainedModel,
        prediction: object,
    ) -> float | None:
        raise NotImplementedError

class ProbabilityConfidenceProvider(
    BaseConfidenceProvider
):

    def supports(
        self,
        trained_model: TrainedModel,
    ) -> bool:

        estimator = get_estimator(
            trained_model.model
        )

        return hasattr(
            estimator,
            "predict_proba",
        )
    def get_confidence(
    self,
    trained_model: TrainedModel,
    feature_values: dict[str, object],
    prediction: object,
) -> float | None:

        estimator = get_estimator(
            trained_model.model
        )

        probabilities = estimator.predict_proba(
            [
                list(feature_values.values())
            ]
        )

        classes = list(
            estimator.classes_
        )

        index = classes.index(
            prediction
        )

        return float(
            probabilities[0][index]
        )

class NullConfidenceProvider(
    BaseConfidenceProvider
):

    def supports(
        self,
        trained_model: TrainedModel,
    ) -> bool:

        return True


    def get_confidence(
        self,
        trained_model: TrainedModel,
        feature_values: dict[str, object],
        prediction: object,
    ) -> float | None:

        return None