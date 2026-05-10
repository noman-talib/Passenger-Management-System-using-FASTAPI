from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from db_connection import Base

class Bookings(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    flight_id = Column(Integer, ForeignKey("flights.id"))
    booking_date = Column(String)
    payment_status = Column(String, default="pending")
    total_amount = Column(Integer)