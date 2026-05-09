class Flights(Base):
    __tablename__ = "flights"
    id = Column(Integer, primary_key=True)
    flight_no = Column(String, unique=True)
    plane_no = Column(String, unique=True)
    from_airport = Column(String)
    to_airport = Column(String)
    departure_time = Column(String)
    arrival_time = Column(String)
    duration = Column(Integer)
    total_seats = Column(Integer)