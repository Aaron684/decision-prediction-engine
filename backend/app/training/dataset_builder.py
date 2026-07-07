from app.training.schemas import TrainingDataset
from app.training.type_converter import (
    convert_feature_value,
    convert_target_value,
)


def build_training_dataset(category) -> TrainingDataset:

    features = sorted(
        category.features,
        key=lambda feature: feature.id,
    )

    X = []
    y = []

    for observation in category.observations:

        values_by_feature = {
            value.feature_id: value.value
            for value in observation.values
        }

        row = []

        for feature in features:
            converted_value = convert_feature_value(
                values_by_feature[feature.id],
                feature.data_type,
            )

            row.append(converted_value)

        X.append(row)

        y.append(
            convert_target_value(
                observation.target_value,
                category.target_type,
            )
        )

    return TrainingDataset(
        X=X,
        y=y,
        feature_names=[
            feature.name
            for feature in features
        ],
        target_name=category.target_name,
        target_type=category.target_type,
    )