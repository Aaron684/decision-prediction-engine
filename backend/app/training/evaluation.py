from sklearn.model_selection import cross_val_predict

from training.cross_validation import get_cv_strategy
from training.metrics import calculate_metrics
from training.schemas import ModelEvaluation


def evaluate_model(
    model_info,
    dataset,
):
    estimator = model_info["factory"]()

    cv = get_cv_strategy(dataset)

    predictions = cross_val_predict(
        estimator,
        dataset.X,
        dataset.y,
        cv=cv,
    )

    primary, secondary = calculate_metrics(
        dataset.y,
        predictions,
        dataset.target_type,
    )

    return ModelEvaluation(
        model_id=model_info["model_id"],
        model_name=model_info["display_name"],
        estimator=estimator,
        primary_score=primary,
        secondary_metrics=secondary,
        cv_strategy=type(cv).__name__,
    )