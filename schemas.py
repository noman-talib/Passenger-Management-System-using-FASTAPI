from pydantic import BaseModel
from typing import Optional

class Passenger(BaseModel):
    name:str
    age:int
    gender:str
    destination:str
    fare:int
    phone_number:str
    cnic:str

class UpdatePassenger(BaseModel):
    name:Optional[str] = None
    age:Optional[int] = None
    gender:Optional[str] = None
    destination:Optional[str] = None
    fare:Optional[str] = None
    phone_number:Optional[str] = None
    cnic:Optional[str] = None
