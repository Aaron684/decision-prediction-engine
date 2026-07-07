from pydantic import BaseModel, ConfigDict
from typing import Literal


class FeatureCreate(BaseModel):
    category_id: int
    name: str
    data_type: Literal["numeric", "boolean"]


class FeatureUpdate(BaseModel):
    name: str | None = None


class FeatureRead(BaseModel):
    id: int
    category_id: int
    name: str
    data_type: str

    model_config = ConfigDict(from_attributes=True)