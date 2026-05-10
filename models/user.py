from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from db_connection import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    cnic = Column(String)
    age = Column(Integer)
    gender = Column(String)
    phone_number = Column(String)
    role = Column(String, default="passenger")