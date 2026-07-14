from sklearn.model_selection import (
    LeaveOneOut,
    KFold,
)

from training.schemas import TrainingDataset


RANDOM_STATE = 42

LOOCV_THRESHOLD = 30
TEN_FOLD_THRESHOLD = 200


def get_cv_strategy(dataset: TrainingDataset):

    observation_count = len(dataset.y)

    if observation_count < LOOCV_THRESHOLD:
        return LeaveOneOut()

    folds = (
        10
        if observation_count >= TEN_FOLD_THRESHOLD
        else 5
    )

    return KFold(
        n_splits=folds,
        shuffle=True,
        random_state=RANDOM_STATE,
    )