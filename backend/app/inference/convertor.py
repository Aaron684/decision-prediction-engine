from app.training.schemas import TrainedModel
from app.training.type_converter import (
    convert_feature_value,
)


def convert_prediction_values(
    trained_model: TrainedModel,
    values: dict[str, object],
) -> list:

    converted_values = []

    for feature in trained_model.features:

        converted_value = convert_feature_value(
            values[feature.name],
            feature.data_type,
        )

        converted_values.append(
            converted_value
        )

    return converted_values