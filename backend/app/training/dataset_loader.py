from sqlalchemy.orm import Session, selectinload

from app.models.category import Category
from app.models.observation import Observation
from app.training.exceptions import DatasetNotFoundError


def load_category_dataset(
    db: Session,
    category_id: int,
) -> Category:

    category = (
        db.query(Category)
        .options(
            selectinload(Category.features),
            selectinload(Category.observations).selectinload(
                Observation.values
            ),
        )
        .filter(Category.id == category_id)
        .first()
    )

    if category is None:
        raise DatasetNotFoundError(
            f"Category with id {category_id} was not found."
        )

    return category

