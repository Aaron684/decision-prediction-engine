from training.evaluation import evaluate_model
from training.leaderboard import ModelLeaderboard
from training.model_factory import get_model_registry
from training.schemas import TrainingDataset, ModelEvaluation


def compare_models(
    dataset: TrainingDataset,
) -> ModelLeaderboard:

    registry = get_model_registry(dataset.target_type)

    evaluations: list[ModelEvaluation] = []

    for _, model_info in registry.items():

        try:
            evaluation = evaluate_model(
                dataset=dataset,
                model_info=model_info,
            )

        except Exception as ex:

            evaluation = ModelEvaluation(
                model_id=model_info["model_id"],
                model_name=model_info["display_name"],
                estimator=None,
                primary_score=0.0,
                secondary_metrics={},
                cv_strategy="Unknown",
                failed=True,
                error_message=str(ex),
            )

        evaluations.append(evaluation)

    return ModelLeaderboard(evaluations)