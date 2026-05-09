class FlightCreate(BaseModel):
    flight_no:str
    plane_no:str
    from_airport:str
    to_airport:str
    arrival_time:str
    departure_time:str
    flight_duration:str
    total_seats:int

    @field_validator("total_seats")
    def seats_Check(cls,value):
        if value <= 0 :
            raise ValueError("Seats Must be positive")
        return value

class FlightUpdate(BaseModel):
    flight_no:Optional[str] = None
    plane_no:Optional[str] = None
    from_airport:Optional[str] = None
    to_airport:Optional[str] = None
    arrival_time:Optional[str] = None
    departure_time:Optional[str] = None
    flight_duration:Optional[str] = None
    total_seats:Optional[int] = None

class FlightResponse(BaseModel):
    id:int
    flight_no:str
    plane_no:str
    from_airport:str
    to_airport:str
    arrival_time:str
    departure_time:str
    flight_duration:str
    total_seats:str
    class Config:
        from_attributes = True