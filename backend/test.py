from app.training.schemas import TrainingDataset
from app.training.pipeline import train_category
from app.training.comparison import compare_models
from app.training.trainer import train_best_model


dataset = TrainingDataset(
    X=[
        [1.0],
        [2.0],
        [3.0],
        [4.0],
        [5.0],
        [6.0],
    ],
    y=[
        1,
        5,
        3,
        4,
        2,
        0.5,
    ],
    feature_names=[
        "test_feature"
    ],
    target_name="outcome",
    target_type="regression",
)

leaderboard = compare_models(dataset)


print(
    leaderboard.evaluations
)

winner = leaderboard.best()

print(
    "winner: " + winner.model_name
)

trained = train_best_model(
    dataset,
    leaderboard,
)


print(trained)

prediction = trained.model.predict(
    [[7.0]]
)

print(prediction)