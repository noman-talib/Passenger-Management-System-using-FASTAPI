from pydantic import BaseModel, field_validator
from typing import Optional

class UserCreate(BaseModel):
    name:str
    email:str
    password:str
    cnic:str
    age:int
    gender:str
    phone_number:str
    role:str


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
    
    @field_validator("password")
    def password_check(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters")
        if len(value) > 72:
            raise ValueError("Password cannot be longer than 72 characters")
        return value
    
    @field_validator("phone_number")
    def phone_check(cls, value):
        if not value.isdigit() or len(value) != 11:
            raise ValueError("Must be a valid value")
        return value
    
    @field_validator("cnic")
    def cnic_check(cls, value):
        if not value.isdigit() or len(value) < 13:
            raise ValueError("Cnic must contain 13 digits")
        return value
    @field_validator("role")
    def role_check(cls, value):
        if value not in ["Admin", "Passenger", "admin", "passenger"]:
            raise ValueError("Role not found")
        return value

class UpdateUser(BaseModel):
    name:Optional[str] = None
    age:Optional[int] = None
    gender:Optional[str] = None
    email:Optional[str] = None
    phone_number:Optional[str] = None
    cnic:Optional[str] = None

class UserLogin(BaseModel):
    email:str
    password:str

class UserResponse(BaseModel):
    id:int
    name:str
    email:str
    role:str
    gender:str
    phone_number:str
    class Config:
        from_attributes = True
