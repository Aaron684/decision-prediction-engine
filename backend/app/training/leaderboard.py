from app.training.schemas import ModelEvaluation


class ModelLeaderboard:

    def __init__(
        self,
        evaluations: list[ModelEvaluation],
    ):
        self.evaluations = evaluations

    def successful_models(
        self,
    ) -> list[ModelEvaluation]:

        return [
            evaluation
            for evaluation in self.evaluations
            if not evaluation.failed
        ]

    def failed_models(
        self,
    ) -> list[ModelEvaluation]:

        return [
            evaluation
            for evaluation in self.evaluations
            if evaluation.failed
        ]

    def best(
        self,
    ) -> ModelEvaluation:

        successful = self.successful_models()

        if not successful:
            raise RuntimeError(
                "No models were successfully evaluated."
            )

        return max(
            successful,
            key=lambda evaluation: evaluation.primary_score,
        )

    def top(
        self,
        n: int,
    ) -> list[ModelEvaluation]:

        successful = sorted(
            self.successful_models(),
            key=lambda evaluation: evaluation.primary_score,
            reverse=True,
        )

        return successful[:n]