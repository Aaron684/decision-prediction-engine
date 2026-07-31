from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.repositories.model_repository import (
    ModelRepository,
)

from app.schemas.training import (
    TrainingResult, ActiveModelResponse
)

from app.training.service import (
    TrainingService,
)



router = APIRouter(
    prefix="/training",
    tags=["Training"],
)

repository = ModelRepository()

service = TrainingService(
    ModelRepository(),
)


@router.post(
    "/categories/{category_id}",
    response_model=TrainingResult,
)
def train_category(
    category_id: int,
    db: Session = Depends(get_db),
):

    return service.train_category(
        db=db,
        category_id=category_id,
    )

@router.get(
    "/categories/{category_id}",
    response_model=ActiveModelResponse | None,
)
def get_active_model_info(
    category_id: int,
    db: Session = Depends(get_db),
):
    model = repository.get_active_model_record(
        db,
        category_id,
    )

    if model is None:
        return None

    return model