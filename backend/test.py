from app.database.database import SessionLocal

from app.training.pipeline import (
    train_category,
)

from app.repositories.model_repository import (
    ModelRepository,
)

from app.inference.schemas import (
    PredictionRequest,
)

from app.inference.service import (
    PredictionService,
)


CATEGORY_ID = 2


def main():

    db = SessionLocal()

    try:

        repository = ModelRepository()


        print("=" * 60)
        print("TRAINING CATEGORY 2 MODEL")
        print("=" * 60)


        # Train model from SQLite data
        trained_model, leaderboard = train_category(
            db,
            CATEGORY_ID,
        )


        print("\nWinner:")
        print(
            trained_model.model_name
        )


        print("\nSaving model...")


        saved_model = repository.save_model(
            db=db,
            category_id=CATEGORY_ID,
            trained_model=trained_model,
            primary_score=leaderboard.best().primary_score,
            secondary_metrics=(
                leaderboard.best().secondary_metrics
            ),
        )


        print("\nSaved Model:")
        print("----------------")
        print(
            f"ID: {saved_model.id}"
        )
        print(
            f"Model: {saved_model.model_name}"
        )
        print(
            f"Version: {saved_model.version}"
        )
        print(
            f"Active: {saved_model.is_active}"
        )


        print("\n")
        print("=" * 60)
        print("RUNNING CLASSIFICATION PREDICTION")
        print("=" * 60)


        service = PredictionService(
            repository
        )


        request = PredictionRequest(
            values={
                "sleep": 8,
                "healthy": "true",
            }
        )


        result = service.predict_category(
            db=db,
            category_id=CATEGORY_ID,
            request=request,
        )


        print("\nPrediction:")
        print(
            result.prediction
        )


        print("\n")
        print("=" * 60)
        print("CLASSIFICATION INFERENCE TEST PASSED")
        print("=" * 60)



    finally:

        db.close()



if __name__ == "__main__":
    main()