from training.comparison import compare_models
from training.dataset_builder import create_training_dataset
from training.trainer import train_best_model


def train_category(
    db,
    category_id: int,
):

    dataset = create_training_dataset(
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

    return trained_model