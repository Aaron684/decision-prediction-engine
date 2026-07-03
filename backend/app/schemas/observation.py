from pydantic import BaseModel, ConfigDict


class ObservationValueCreate(BaseModel):
    feature_id: int
    value: str


class ObservationCreate(BaseModel):
    category_id: int
    target_value: str
    values: list[ObservationValueCreate]


class ObservationValueRead(BaseModel):
    feature_id: int
    feature_name: str
    value: str

    model_config = ConfigDict(from_attributes=True)


class ObservationRead(BaseModel):
    id: int
    category_id: int
    target_value: str
    values: list[ObservationValueRead]

    model_config = ConfigDict(from_attributes=True)