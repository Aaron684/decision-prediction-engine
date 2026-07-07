from app.training.exceptions import (
    DuplicateFeatureValueError,
    InsufficientDataError,
    InvalidFeatureValueError,
    InvalidTargetValueError,
    MissingFeatureError,
    UnexpectedFeatureError,
)
from app.training.type_converter import (
    convert_feature_value,
    convert_target_value,
)


def validate_dataset(category):
    """
    Validate that a category contains a complete,
    trainable dataset.
    """

    if not category.features:
        raise InsufficientDataError(
            f"Category '{category.name}' has no features."
        )

    if not category.observations:
        raise InsufficientDataError(
            f"Category '{category.name}' has no observations."
        )

    feature_map = {
        feature.id: feature
        for feature in category.features
    }

    for observation in category.observations:
        validate_observation(
            observation,
            feature_map,
            category.target_type,
        )

    validate_target_distribution(
        category
    )

    return True

def validate_observation(
    observation,
    feature_map,
    target_type,
):
    values_seen = set()

    for value in observation.values:

        if value.feature_id not in feature_map:
            raise UnexpectedFeatureError(
                f"Observation {observation.id} contains "
                f"unknown feature id {value.feature_id}."
            )

        if value.feature_id in values_seen:
            feature = feature_map[value.feature_id]

            raise DuplicateFeatureValueError(
                f"Observation {observation.id} contains "
                f"duplicate values for feature '{feature.name}'."
            )

        values_seen.add(value.feature_id)

        feature = feature_map[value.feature_id]

        if value.value is None:
            raise InvalidFeatureValueError(
                f"Feature '{feature.name}' "
                f"has no value."
            )

        try:
            convert_feature_value(
                value.value,
                feature.data_type,
            )

        except Exception as exc:
            raise InvalidFeatureValueError(
                f"Feature '{feature.name}' "
                f"has invalid value '{value.value}'."
            ) from exc

    missing_features = (
        set(feature_map.keys())
        -
        values_seen
    )

    if missing_features:
        missing_feature = feature_map[
            missing_features.pop()
        ]

        raise MissingFeatureError(
            f"Observation {observation.id} "
            f"is missing feature '{missing_feature.name}'."
        )

    if observation.target_value is None:
        raise InvalidTargetValueError(
            f"Observation {observation.id} "
            "has no target value."
        )

    try:
        convert_target_value(
            observation.target_value,
            target_type,
        )

    except Exception as exc:
        raise InvalidTargetValueError(
            f"Observation {observation.id} "
            f"has invalid target value "
            f"'{observation.target_value}'."
        ) from exc
    
def validate_target_distribution(category):
    if category.target_type != "classification":
        return

    targets = {
        observation.target_value
        for observation in category.observations
    }

    if len(targets) < 2:
        raise InsufficientDataError(
            "Classification datasets require "
            "at least two target classes."
        )