from pydantic import BaseModel


class PredictionRequest(BaseModel):

    values: dict[str, object]


class PredictionResult(BaseModel):

    prediction: object