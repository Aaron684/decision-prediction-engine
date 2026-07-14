from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    r2_score,
    mean_absolute_error,
    mean_squared_error,
)

import math


def calculate_metrics(
    y_true,
    y_pred,
    target_type: str,
):

    if target_type == "classification":
        return _classification_metrics(
            y_true,
            y_pred,
        )

    if target_type == "regression":
        return _regression_metrics(
            y_true,
            y_pred,
        )

    raise ValueError(
        f"Unsupported target type: {target_type}"
    )


def _classification_metrics(
    y_true,
    y_pred,
):

    primary = f1_score(
        y_true,
        y_pred,
        zero_division=0,
    )

    secondary = {
        "accuracy": accuracy_score(
            y_true,
            y_pred,
        ),

        "precision": precision_score(
            y_true,
            y_pred,
            zero_division=0,
        ),

        "recall": recall_score(
            y_true,
            y_pred,
            zero_division=0,
        ),
    }

    return primary, secondary


def _regression_metrics(
    y_true,
    y_pred,
):

    primary = r2_score(
        y_true,
        y_pred,
    )

    mse = mean_squared_error(
        y_true,
        y_pred,
    )

    secondary = {
        "mae": mean_absolute_error(
            y_true,
            y_pred,
        ),

        "rmse": math.sqrt(mse),
    }

    return primary, secondary