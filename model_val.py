from pydantic import BaseModel,Field
from typing import Optional


class emp(BaseModel):
    id:int= Field(...,gt=0)
    name:str=Field(...,min_length=3)
    department:str=Field(...,max_length=2)
    age:Optional[int]=Field(default='none')

