from pydantic import BaseModel, field_validator
from typing import Optional

class Passenger(BaseModel):
    name:str
    age:int
    gender:str
    destination:str
    fare:int
    phone_number:str
    cnic:str

    @field_validator("name")
    def name_check(cls, value):
        if not value.replace(" ", "").isalpha():
            raise ValueError("Name should contains only letters")
        return value
    @field_validator("age")
    def age_check(cls, value):
        if value < 1 or value > 100:
            raise ValueError("Age must be greater than 1 and less than 100")
        return value
    @field_validator("gender")
    def gender_check(cls, value):
        if value not in ["Male", "Female", "male", "female"]:
            raise ValueError("Gender should be male or female")
        return value
    
    @field_validator("destination")
    def destination_check(cls, value):
        if not value.replace(" ", "").isalpha():
            raise ValueError("Must be a valid value")
        return value
    
    @field_validator("fare")
    def fare_check(cls, value):
        if value  < 1 or value > 100:
            raise ValueError("Must be a valid value")
        return value
    
    @field_validator("phone_number")
    def phone_check(cls, value):
        if not value.isdigit() or len(value) <= 11:
            raise ValueError("Must be a valid value")
        return value
    
    @field_validator("cnic")
    def cnic_check(cls, value):
        if not value.isdigit() or len(value) < 13:
            raise ValueError("Cnic must contain 13 digits")
        return value

class UpdatePassenger(BaseModel):
    name:Optional[str] = None
    age:Optional[int] = None
    gender:Optional[str] = None
    destination:Optional[str] = None
    fare:Optional[str] = None
    phone_number:Optional[str] = None
    cnic:Optional[str] = None
