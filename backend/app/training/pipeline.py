from sqlalchemy.orm import Session

from app.training.dataset_loader import load_category_dataset
from app.training.dataset_builder import build_training_dataset
from app.training.validator import validate_dataset
from app.training.schemas import TrainingDataset


def create_training_dataset(
    db: Session,
    category_id: int,
) -> TrainingDataset:
    """
    Create a validated machine learning dataset
    from a category.
    """

    category = load_category_dataset(
        db,
        category_id,
    )

    validate_dataset(category)

    return build_training_dataset(category)