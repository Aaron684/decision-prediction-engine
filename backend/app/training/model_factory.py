from sklearn.linear_model import (
    LinearRegression,
    LogisticRegression,
)


CLASSIFICATION_MODELS = {
    "logistic_regression": {
        "display_name": "Logistic Regression",
        "model_id": "logistic_regression",
        "factory": lambda: LogisticRegression(max_iter=1000),
    },
}

REGRESSION_MODELS = {
    "linear_regression": {
        "display_name": "Linear Regression",
        "model_id": "linear_regression",
        "factory": lambda: LinearRegression(),
    },
}


def create_model(target_type: str):

    registry = get_model_registry(target_type)

    _, model_info = next(iter(registry.items()))

    return model_info["factory"]()


def get_model_registry(target_type: str):

    if target_type == "classification":
        return CLASSIFICATION_MODELS

    if target_type == "regression":
        return REGRESSION_MODELS

    raise ValueError(
        f"Unsupported target type: {target_type}"
    )
def get_model_info(
    target_type: str,
    model_id: str,
) -> dict:

    registry = get_model_registry(target_type)

    try:
        return registry[model_id]
    except KeyError:
        raise ValueError(
            f"Unknown model: {model_id}"
        )


def create_registered_model(
    target_type: str,
    model_id: str,
):

    model_info = get_model_info(
        target_type,
        model_id,
    )

    return model_info["factory"]()