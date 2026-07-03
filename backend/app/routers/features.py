from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.category import Category
from app.models.feature import Feature
from app.schemas.feature import (
    FeatureCreate,
    FeatureRead,
    FeatureUpdate,
)

router = APIRouter(
    prefix="/features",
    tags=["Features"],
)

@router.post("/", response_model=FeatureRead, status_code=201)
def create_feature(
    feature_data: FeatureCreate,
    db: Session = Depends(get_db),
):
    # Verify the parent category exists.
    category = db.get(Category, feature_data.category_id)

    if category is None:
        raise HTTPException(
            status_code=404,
            detail="Category not found",
        )

    # Ensure the feature name is unique within the category.
    existing_feature = (
        db.query(Feature)
        .filter(
            Feature.category_id == feature_data.category_id,
            Feature.name == feature_data.name,
        )
        .first()
    )

    if existing_feature is not None:
        raise HTTPException(
            status_code=409,
            detail="A feature with this name already exists in the category.",
        )

    feature = Feature(
        category_id=feature_data.category_id,
        name=feature_data.name,
        data_type=feature_data.data_type,
    )

    db.add(feature)
    db.commit()
    db.refresh(feature)

    return feature

@router.get("/", response_model=list[FeatureRead])
def get_features(
    category_id: int | None = None,
    db: Session = Depends(get_db),
):
    query = db.query(Feature)

    if category_id is not None:
        query = query.filter(Feature.category_id == category_id)

    return query.all()


@router.get("/{feature_id}", response_model=FeatureRead)
def get_feature(
    feature_id: int,
    db: Session = Depends(get_db),
):
    feature = db.get(Feature, feature_id)

    if feature is None:
        raise HTTPException(
            status_code=404,
            detail="Feature not found",
        )

    return feature

@router.put("/{feature_id}", response_model=FeatureRead)
def update_feature(
    feature_id: int,
    feature_data: FeatureUpdate,
    db: Session = Depends(get_db),
):
    feature = db.get(Feature, feature_id)

    if feature is None:
        raise HTTPException(
            status_code=404,
            detail="Feature not found",
        )

    update_data = feature_data.model_dump(exclude_unset=True)

    if "name" in update_data:
        existing_feature = (
            db.query(Feature)
            .filter(
                Feature.category_id == feature.category_id,
                Feature.name == update_data["name"],
                Feature.id != feature.id,
            )
            .first()
        )

        if existing_feature is not None:
            raise HTTPException(
                status_code=409,
                detail="A feature with this name already exists in the category.",
            )

    for field, value in update_data.items():
        setattr(feature, field, value)

    db.commit()
    db.refresh(feature)

    return feature

@router.delete("/{feature_id}", status_code=204)
def delete_feature(
    feature_id: int,
    db: Session = Depends(get_db),
):
    feature = db.get(Feature, feature_id)

    if feature is None:
        raise HTTPException(
            status_code=404,
            detail="Feature not found",
        )

    db.delete(feature)
    db.commit()

    return Response(status_code=204)