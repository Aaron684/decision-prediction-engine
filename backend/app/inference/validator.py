from app.inference.exceptions import (
    InvalidPredictionInputError,
)
from app.inference.schemas import (
    PredictionRequest,
)
from app.training.schemas import (
    TrainedModel,
)


def validate_prediction_request(
    trained_model: TrainedModel,
    request: PredictionRequest,
):

    expected = {
        feature.name
        for feature in trained_model.features
    }

    supplied = set(
        request.values.keys()
    )


    missing = expected - supplied

    if missing:

        raise InvalidPredictionInputError(
            f"Missing features: {sorted(missing)}"
        )


    unexpected = supplied - expected

    if unexpected:

        raise InvalidPredictionInputError(
            f"Unexpected features: {sorted(unexpected)}"
        )