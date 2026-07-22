from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.inference.schemas import (
    PredictionRequest,
)

from app.inference.service import (
    PredictionService,
)

from app.repositories.model_repository import (
    ModelRepository,
)


router = APIRouter(
    prefix="/predict",
    tags=["Prediction"],
)


service = PredictionService(
    ModelRepository()
)


@router.post(
    "/categories/{category_id}"
)
def predict_category(
    category_id: int,
    request: PredictionRequest,
    db: Session = Depends(get_db),
):

    result = service.predict_category(
        db=db,
        category_id=category_id,
        request=request,
    )


    return {
        "prediction": result.prediction
    }