from uuid import uuid4, UUID
from pydantic import BaseModel
from typing import Optional, Union


#  I am aware that this is not the best way to do it (open to suggestions)
class Recipe(BaseModel):
    id: Optional[UUID] = uuid4()
    title: str
    rating: Optional[int]
    calories: Optional[Union[str, float]]
    protein: Optional[Union[str, float]]
    fat: Optional[Union[str, float]]
    sodium: Optional[Union[str, float]]
    almond: Optional[int]
    dairy: Optional[int]
    pork: Optional[int]


class RecipeUpdateRequest(BaseModel):
    title: Optional[str]
    rating: Optional[str]
    calories: Optional[Union[str, float]]
    protein: Optional[Union[str, float]]
    fat: Optional[Union[str, float]]
    sodium: Optional[Union[str, float]]
    almond: Optional[str]
    dairy: Optional[str]
    pork: Optional[str]
