from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import declarative_base, sessionmaker
from db_connection import Base
class Passenger(Base):
    __tablename__ = "passengers"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    cnic = Column(String)
    age = Column(Integer)
    gender = Column(String)
    destination = Column(String)
    fare = Column(Integer)
    phone_number = Column(Integer)

    

