from app.training.dataset_builder import (
    build_training_dataset,
)

from app.training.comparison import (
    compare_models,
)

from app.training.trainer import (
    train_best_model,
)


def train_category(
    db,
    category_id: int,
):

    dataset = build_training_dataset(
        db,
        category_id,
    )


    leaderboard = compare_models(
        dataset,
    )


    trained_model = train_best_model(
        dataset,
        leaderboard,
    )


    return (
        trained_model,
        leaderboard,
    )