from pathlib import Path

import joblib
from sqlalchemy.orm import Session

from app.models.trained_models import TrainedModel as TrainedModelDB
from app.training.schemas import TrainedModel


MODEL_STORAGE_PATH = Path("storage/models")


class ModelRepository:

    def save_model(
        self,
        db: Session,
        category_id: int,
        trained_model: TrainedModel,
        primary_score: float,
        secondary_metrics: dict[str, float] | None = None,
    ) -> TrainedModelDB:

        category_folder = (
            MODEL_STORAGE_PATH /
            f"category_{category_id}"
        )

        category_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        version = self._get_next_version(
            db,
            category_id,
        )

        filename = (
            f"{trained_model.model_id}"
            f"_v{version}.pkl"
        )

        model_path = category_folder / filename

        joblib.dump(
            trained_model,
            model_path,
        )

        db_model = TrainedModelDB(
            category_id=category_id,
            model_id=trained_model.model_id,
            model_name=trained_model.model_name,
            version=version,
            model_path=str(model_path),
            observation_count=trained_model.observation_count,
            primary_score=primary_score,
            secondary_metrics=secondary_metrics,
            is_active=True,
        )

        self._deactivate_existing_models(
            db,
            category_id,
        )

        db.add(db_model)
        db.commit()
        db.refresh(db_model)

        return db_model


    def _get_next_version(
        self,
        db: Session,
        category_id: int,
    ) -> int:

        models = (
            db.query(TrainedModelDB)
            .filter(
                TrainedModelDB.category_id == category_id
            )
            .all()
        )

        if not models:
            return 1

        return max(
            model.version
            for model in models
        ) + 1


    def _deactivate_existing_models(
        self,
        db: Session,
        category_id: int,
    ):

        models = (
            db.query(TrainedModelDB)
            .filter(
                TrainedModelDB.category_id == category_id
            )
            .all()
        )

        for model in models:
            model.is_active = False

    def load_model(
        self,
        db: Session,
        model_record_id: int,
    ) -> TrainedModel:

        db_model = (
            db.query(TrainedModelDB)
            .filter(
                TrainedModelDB.id == model_record_id
            )
            .first()
        )

        if db_model is None:
            raise ValueError(
                "Model not found."
            )

        return joblib.load(
            db_model.model_path
        )
    
    def list_models(
        self,
        db: Session,
        category_id: int,
    ) -> list[TrainedModelDB]:

        return (
            db.query(TrainedModelDB)
            .filter(
                TrainedModelDB.category_id == category_id
            )
            .order_by(
                TrainedModelDB.version.desc()
            )
            .all()
    )

    def get_active_model(
        self,
        db: Session,
        category_id: int,
    )-> TrainedModel:

        active = (
            db.query(TrainedModelDB)
            .filter(
                TrainedModelDB.category_id == category_id,
                TrainedModelDB.is_active == True,
            )
            .first()
        )

        if active is None:
            raise ValueError(
                "No active model found."
            )

        return self.load_model(
            db,
            active.id,
        )
    
    def activate_model(
        self,
        db: Session,
        model_record_id: int,
    ) -> None:

        model = (
            db.query(TrainedModelDB)
            .filter(
                TrainedModelDB.id == model_record_id
            )
            .first()
        )

        if model is None:
            raise ValueError(
                "Model not found."
            )

        self._deactivate_existing_models(
            db,
            model.category_id,
        )

        model.is_active = True

        db.commit()

    def delete_model(
        self,
        db: Session,
        model_record_id: int,
    ) -> None:

        model = (
            db.query(TrainedModelDB)
            .filter(
                TrainedModelDB.id == model_record_id
            )
            .first()
        )

        if model is None:
            raise ValueError(
                "Model not found."
            )

        was_active = model.is_active
        category_id = model.category_id

        path = Path(model.model_path)

        if path.exists():
            path.unlink()

        db.delete(model)

        db.flush()

        if was_active:
            self._promote_latest_model(
                db,
                category_id,
            )

        db.commit()

    def _promote_latest_model(
        self,
        db: Session,
        category_id: int,
):

        newest = (
            db.query(TrainedModelDB)
            .filter(
                TrainedModelDB.category_id == category_id
            )
            .order_by(
                TrainedModelDB.version.desc()
            )
            .first()
        )

        if newest is not None:
            newest.is_active = True