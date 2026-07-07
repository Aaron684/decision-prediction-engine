from pydantic import BaseModel, ConfigDict
from typing import Literal


class CategoryCreate(BaseModel):
    name: str
    description: str | None = None
    target_name: str
    target_type: Literal["classification", "regression"]

class CategoryUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    target_name: str | None = None

class CategoryRead(BaseModel):
    id: int
    name: str
    description: str | None = None
    target_name: str
    target_type: str

    model_config = ConfigDict(from_attributes=True)