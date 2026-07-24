from sklearn.pipeline import Pipeline


def get_estimator(model):

    if isinstance(model, Pipeline):
        return model[-1]

    return model