from pydantic import BaseModel, field_validator
from typing import Optional

class BookingCreate(BaseModel):
    flight_id:int
    total_amount:int

class BookingResponse(BaseModel):
    name:str
    flight_id:int
    booking_Date_and_Time:str
    payment_status:str
    total_amount:int
    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str