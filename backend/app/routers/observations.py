from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session, selectinload

from app.database.dependencies import get_db
from app.models.category import Category
from app.models.feature import Feature
from app.models.observation import Observation
from app.models.observation_value import ObservationValue
from app.schemas.observation import (
    ObservationCreate,
    ObservationRead,
)

router = APIRouter(
    prefix="/observations",
    tags=["Observations"],
)

@router.post("/", response_model=ObservationRead, status_code=201)
def create_observation(
    observation_data: ObservationCreate,
    db: Session = Depends(get_db),
):

    category = db.get(Category, observation_data.category_id)

    if category is None:
        raise HTTPException(
            status_code=404,
            detail="Category not found",
        )

    category_features = (
        db.query(Feature)
        .filter(Feature.category_id == observation_data.category_id)
        .all()
    )

    category_feature_ids = {
        feature.id
        for feature in category_features
    }

    submitted_feature_ids = {
        value.feature_id
        for value in observation_data.values
    }

    if len(submitted_feature_ids) != len(observation_data.values):
        raise HTTPException(
            status_code=400,
            detail="Duplicate feature IDs are not allowed.",
        )

    invalid_features = (
        submitted_feature_ids
        - category_feature_ids
    )

    if invalid_features:
        raise HTTPException(
            status_code=400,
            detail="One or more feature IDs do not belong to this category.",
        )

    missing_features = (
        category_feature_ids
        - submitted_feature_ids
    )

    if missing_features:
        raise HTTPException(
            status_code=400,
            detail="Every feature in the category must have exactly one value.",
        )

    observation = Observation(
        category_id=observation_data.category_id,
        target_value=observation_data.target_value,
    )

    db.add(observation)
    db.flush()

    for value in observation_data.values:
        observation_value = ObservationValue(
            observation_id=observation.id,
            feature_id=value.feature_id,
            value=value.value,
        )

        db.add(observation_value)

    db.commit()
    db.refresh(observation)

    return observation

@router.get("/", response_model=list[ObservationRead])
def get_observations(
    category_id: int | None = None,
    db: Session = Depends(get_db),
):
    query = (
        db.query(Observation)
        .options(
            selectinload(Observation.values)
            .selectinload(ObservationValue.feature)
        )
    )

    if category_id is not None:
        query = query.filter(
            Observation.category_id == category_id
        )

    return query.all()

@router.get("/{observation_id}", response_model=ObservationRead)
def get_observation(
    observation_id: int,
    db: Session = Depends(get_db),
):
    observation = (
        db.query(Observation)
        .options(
            selectinload(Observation.values)
            .selectinload(ObservationValue.feature)
        )
        .filter(Observation.id == observation_id)
        .first()
    )

    if observation is None:
        raise HTTPException(
            status_code=404,
            detail="Observation not found",
        )

    return observation

@router.put("/{observation_id}", response_model=ObservationRead)
def update_observation(
    observation_id: int,
    observation_data: ObservationCreate,
    db: Session = Depends(get_db),
):
    observation = (
        db.query(Observation)
        .options(selectinload(Observation.values))
        .filter(Observation.id == observation_id)
        .first()
    )

    if observation is None:
        raise HTTPException(
            status_code=404,
            detail="Observation not found",
        )

    # Ensure the category isn't being changed.
    if observation.category_id != observation_data.category_id:
        raise HTTPException(
            status_code=400,
            detail="An observation cannot be moved to another category.",
        )

    category_features = (
        db.query(Feature)
        .filter(Feature.category_id == observation.category_id)
        .all()
    )

    category_feature_ids = {
        feature.id
        for feature in category_features
    }

    submitted_feature_ids = {
        value.feature_id
        for value in observation_data.values
    }

    if len(submitted_feature_ids) != len(observation_data.values):
        raise HTTPException(
            status_code=400,
            detail="Duplicate feature IDs are not allowed.",
        )

    invalid_features = (
        submitted_feature_ids
        - category_feature_ids
    )

    if invalid_features:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid feature IDs: {sorted(invalid_features)}",
        )

    missing_features = (
        category_feature_ids
        - submitted_feature_ids
    )

    if missing_features:
        raise HTTPException(
            status_code=400,
            detail=f"Missing feature IDs: {sorted(missing_features)}",
        )

    observation.target_value = observation_data.target_value

    for value in observation.values:
        db.delete(value)

    db.flush()

    for value in observation_data.values:
        db.add(
            ObservationValue(
                observation_id=observation.id,
                feature_id=value.feature_id,
                value=value.value,
            )
        )

    db.commit()
    db.refresh(observation)

    return observation

@router.delete("/{observation_id}", status_code=204)
def delete_observation(
    observation_id: int,
    db: Session = Depends(get_db),
):
    observation = db.get(Observation, observation_id)

    if observation is None:
        raise HTTPException(
            status_code=404,
            detail="Observation not found",
        )

    db.delete(observation)
    db.commit()

    return Response(status_code=204)