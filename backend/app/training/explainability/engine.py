from app.training.explainability.importance import (
    BaseImportanceProvider,
    CoefficientImportanceProvider,
    TreeImportanceProvider,
)

from app.training.explainability.confidence import (
    BaseConfidenceProvider,
    ProbabilityConfidenceProvider,
    NullConfidenceProvider,
)


IMPORTANCE_PROVIDERS: list[BaseImportanceProvider] = [
    CoefficientImportanceProvider(),
    TreeImportanceProvider(),
]


CONFIDENCE_PROVIDERS: list[BaseConfidenceProvider] = [
    ProbabilityConfidenceProvider(),
    NullConfidenceProvider(),
]

from app.training.schemas import TrainedModel

from app.training.explainability.schemas import (
    PredictionExplanation,
)

def get_importance_provider(
    trained_model: TrainedModel,
) -> BaseImportanceProvider:

    for provider in IMPORTANCE_PROVIDERS:

        if provider.supports(trained_model):
            return provider

    raise ValueError(
        "No importance provider available"
    )

def get_confidence_provider(
    trained_model: TrainedModel,
) -> BaseConfidenceProvider:

    for provider in CONFIDENCE_PROVIDERS:

        if provider.supports(trained_model):
            return provider

    raise ValueError(
        "No confidence provider available"
    )

class ExplanationEngine:

    def explain(
        self,
        trained_model: TrainedModel,
        feature_values: dict[str, object],
        prediction: object,
    ) -> PredictionExplanation:

        importance_provider = (
            get_importance_provider(
                trained_model
            )
        )

        contributions = (
            importance_provider.get_feature_contributions(
                trained_model,
                feature_values,
            )
        )


        confidence_provider = (
            get_confidence_provider(
                trained_model
            )
        )

        confidence = (
            confidence_provider.get_confidence(
                trained_model,
                feature_values,
                prediction,
            )
        )


        return PredictionExplanation(
            method=(
                importance_provider.method_name
            ),
            confidence=confidence,
            feature_contributions=contributions,
        )