from app.inference.convertor import (
    convert_prediction_values,
)

from app.inference.exceptions import (
    PredictionExecutionError,
)

from app.inference.schemas import (
    PredictionRequest,
    PredictionResult,
)

from app.training.schemas import (
    TrainedModel,
)


def predict(
    trained_model: TrainedModel,
    request: PredictionRequest,
) -> PredictionResult:

    values = convert_prediction_values(
        trained_model,
        request.values,
    )

    try:

        prediction = trained_model.model.predict(
            [
                values
            ]
        )[0]

        if hasattr(prediction, "item"):
            prediction = prediction.item()

    except Exception as error:

        raise PredictionExecutionError(
            str(error)
        )


    return PredictionResult(
        prediction=prediction,
    )