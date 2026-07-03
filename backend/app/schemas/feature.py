from pydantic import BaseModel, ConfigDict


class FeatureCreate(BaseModel):
    category_id: int
    name: str
    data_type: str


class FeatureUpdate(BaseModel):
    name: str | None = None


class FeatureRead(BaseModel):
    id: int
    category_id: int
    name: str
    data_type: str

    model_config = ConfigDict(from_attributes=True)