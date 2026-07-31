from pydantic import BaseModel


class TrainingResult(BaseModel):
    model_name: str
    model_id: str

    observation_count: int

    primary_score: float




class ActiveModelResponse(BaseModel):
    id: int
    model_name: str
    version: int
    observation_count: int
    primary_score: float
    is_active: bool