from app.database.database import SessionLocal
from app.training.pipeline import create_training_dataset


db = SessionLocal()

try:
    dataset = create_training_dataset(
        db,
        1,
    )

    print("Features:")
    print(dataset.feature_names)

    print("\nX:")
    for row in dataset.X:
        print(row)

    print("\ny:")
    print(dataset.y)

    print("\nTarget:")
    print(dataset.target_name)

    print("\nType:")
    print(dataset.target_type)

finally:
    db.close()