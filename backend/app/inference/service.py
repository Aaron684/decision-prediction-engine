from sqlalchemy.orm import Session

from app.repositories.model_repository import (
    ModelRepository,
)

from app.inference.schemas import (
    PredictionRequest,
    PredictionResult,
)

from app.inference.validator import (
    validate_prediction_request,
)

from app.inference.predictor import (
    predict,
)

from app.inference.exceptions import (
    ActiveModelNotFoundError,
)


class PredictionService:


    def __init__(
        self,
        repository: ModelRepository,
    ):

        self.repository = repository


    def predict_category(
        self,
        db: Session,
        category_id: int,
        request: PredictionRequest,
    ) -> PredictionResult:


        trained_model = (
            self.repository.get_active_model(
            db,
            category_id,
        )   
    )


        if trained_model is None:

            raise ActiveModelNotFoundError(
                "No active model exists for this category."
            )

        validate_prediction_request(
            trained_model,
            request,
        )
        return predict(
            trained_model,
            request,
        )   