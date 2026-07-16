from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC

from sklearn.linear_model import Ridge
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR

RANDOM_STATE = 42

CLASSIFICATION_MODELS = {
    "logistic_regression": {
        "display_name": "Logistic Regression",
        "model_id": "logistic_regression",
        "factory": lambda: Pipeline(
    [
        ("scaler", StandardScaler()),
        (
            "classifier",
            LogisticRegression(
                max_iter=1000
            ),
        ),
    ]
),
    },
    "decision_tree": {
    "model_id": "decision_tree",
    "display_name": "Decision Tree",
    "factory": lambda: DecisionTreeClassifier(
        random_state=RANDOM_STATE
    ),
    },
    "random_forest": {
    "model_id": "random_forest",
    "display_name": "Random Forest",
    "factory": lambda: RandomForestClassifier(
        n_estimators=100,
        random_state=RANDOM_STATE,
    ),
    },
    "gaussian_naive_bayes": {
    "model_id": "gaussian_naive_bayes",
    "display_name": "Gaussian Naive Bayes",
    "factory": lambda: GaussianNB(),
},
    "gradient_boosting": {
    "model_id": "gradient_boosting",
    "display_name": "Gradient Boosting",
    "factory": lambda: GradientBoostingClassifier(
        random_state=RANDOM_STATE,
    ),
},
    "support_vector_machine": {
    "model_id": "support_vector_machine",
    "display_name": "Support Vector Machine",
    "factory": lambda: Pipeline(
        [
            ("scaler", StandardScaler()),
            (
                "classifier",
                SVC(
                    kernel="rbf",
                    probability=True,
                    random_state=RANDOM_STATE,
                ),
            ),
        ]
    ),
},

}

REGRESSION_MODELS = {
    "ridge_regression": {
    "model_id": "ridge_regression",
    "display_name": "Ridge Regression",
    "factory": lambda: Pipeline(
        [
            ("scaler", StandardScaler()),
            (
                "regressor",
                Ridge(),
            ),
        ]
    ),
},
    "linear_regression": {
    "model_id": "linear_regression",
    "display_name": "Linear Regression",
    "factory": lambda: Pipeline(
        [
            ("scaler", StandardScaler()),
            (
                "regressor",
                LinearRegression(),
            ),
        ]
    ),
},
    "decision_tree_regressor": {
    "model_id": "decision_tree_regressor",
    "display_name": "Decision Tree Regressor",
    "factory": lambda: DecisionTreeRegressor(
        random_state=RANDOM_STATE,
    ),
},
    "random_forest_regressor": {
    "model_id": "random_forest_regressor",
    "display_name": "Random Forest Regressor",
    "factory": lambda: RandomForestRegressor(
        n_estimators=100,
        random_state=RANDOM_STATE,
    ),
},
    "gradient_boosting_regressor": {
    "model_id": "gradient_boosting_regressor",
    "display_name": "Gradient Boosting Regressor",
    "factory": lambda: GradientBoostingRegressor(
        random_state=RANDOM_STATE,
    ),
},
    "support_vector_regressor": {
    "model_id": "support_vector_regressor",
    "display_name": "Support Vector Regressor",
    "factory": lambda: Pipeline(
        [
            ("scaler", StandardScaler()),
            (
                "regressor",
                SVR(kernel="rbf"),
            ),
        ]
    ),
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