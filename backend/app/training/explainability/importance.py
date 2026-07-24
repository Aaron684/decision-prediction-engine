from abc import ABC, abstractmethod

from app.training.schemas import (
    TrainedModel,
)

from app.training.explainability.schemas import (
    FeatureContribution,
)

from app.training.explainability.utils import (
    get_estimator,
)


class BaseImportanceProvider(ABC):

    method_name: str

    @abstractmethod
    def supports(
        self,
        trained_model: TrainedModel,
    ) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_feature_contributions(
        self,
        trained_model: TrainedModel,
        feature_values: dict[str, object],
    ) -> list[FeatureContribution]:
        raise NotImplementedError


class CoefficientImportanceProvider(
    BaseImportanceProvider,
):

    method_name = "coefficients"

    def supports(
        self,
        trained_model: TrainedModel,
    ) -> bool:

        estimator = get_estimator(
            trained_model.model,
        )

        return hasattr(
            estimator,
            "coef_",
        )

    def get_feature_contributions(
        self,
        trained_model: TrainedModel,
        feature_values: dict[str, object],
    ) -> list[FeatureContribution]:

        estimator = get_estimator(
            trained_model.model,
        )

        coefficients = estimator.coef_

        if hasattr(coefficients, "ndim") and coefficients.ndim > 1:
            coefficients = coefficients[0]

        contributions: list[FeatureContribution] = []

        for feature, coefficient in zip(
            trained_model.features,
            coefficients,
        ):

            contributions.append(
                FeatureContribution(
                    feature_name=feature.name,
                    feature_value=feature_values.get(
                        feature.name,
                    ),
                    importance=abs(float(coefficient)),
                    direction=(
                        "positive"
                        if coefficient >= 0
                        else "negative"
                    ),
                )
            )

        contributions.sort(
            key=lambda contribution: contribution.importance,
            reverse=True,
        )

        return contributions


class TreeImportanceProvider(
    BaseImportanceProvider,
):

    method_name = "tree_importance"

    def supports(
        self,
        trained_model: TrainedModel,
    ) -> bool:

        estimator = get_estimator(
            trained_model.model,
        )

        return hasattr(
            estimator,
            "feature_importances_",
        )

    def get_feature_contributions(
        self,
        trained_model: TrainedModel,
        feature_values: dict[str, object],
    ) -> list[FeatureContribution]:

        estimator = get_estimator(
            trained_model.model,
        )

        importances = estimator.feature_importances_

        contributions: list[FeatureContribution] = []

        for feature, importance in zip(
            trained_model.features,
            importances,
        ):

            contributions.append(
                FeatureContribution(
                    feature_name=feature.name,
                    feature_value=feature_values.get(
                        feature.name,
                    ),
                    importance=float(importance),
                    direction=None,
                )
            )

        contributions.sort(
            key=lambda contribution: contribution.importance,
            reverse=True,
        )

        return contributions