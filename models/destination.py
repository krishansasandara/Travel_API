from enum import Enum
from typing import List
from pydantic import BaseModel, Field


class Province(str,Enum): #python support multiple inheritance
    WESTERN = "western"
    CENTRAL = "central"
    SOUTHERN = "southern"
    NORTHERN = "northern"
    EASTERN = "eastern"
    NORTH_WESTERN = "north_western"
    NORTH_CENTRAL = "north_central"
    UVA = "uva"
    SABARAGAMUWA = "sabaragamuwa"

class Category(str,Enum):
    BEACH = "beach"
    HERITAGE = "heritage"
    WILDLIFE = "wildlife"
    HILL_COUNTRY = "hill_country"
    TEMPLE = "temple"
    ADVENTURE = "adventure"

class DestinationCreate(BaseModel):
    name : str = Field(...,min_length=3,max_length=100) #anniwaryai
    city : str = Field(...,min_length=3,max_length=50)
    province : Province
    category : Category
    description : str = Field("",max_length=5000)
    entry_fee : float = Field(0,ge=0) #ge = greater than
    rating : int =  Field(0,ge=0, le=5)
    is_unesco : bool = False
    tags : List[str] = Field(default_factory=list, examples=["ancient","travel"])

class DestinationResponse(BaseModel):
    name: str
    city: str
    province: Province
    category: Category
    description: str
    entry_fee: float
    rating: int
    is_unesco: bool
    tags: List[str]
    created_at : str
    updated_at : str


