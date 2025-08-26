from pydantic import BaseModel


class emp(BaseModel):
    id:int
    name:str
    department:str
    age:int

