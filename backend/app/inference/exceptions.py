class PredictionError(Exception):
    pass


class ActiveModelNotFoundError(
    PredictionError
):
    pass


class InvalidPredictionInputError(
    PredictionError
):
    pass


class PredictionExecutionError(
    PredictionError
):
    pass