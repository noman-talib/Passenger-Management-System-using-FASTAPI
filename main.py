from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db_connection import engine, Base
import models.user
import models.flight
import models.booking
from routes.auth import router as auth_router

app = FastAPI()

Base.metadata.create_all(bind=engine)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)

# @app.get("/")
# def read_base():
#     return{"message": "Welcome to the Passenger Management System"}

# @app.post("/Passengers")
# def add_passenger(passenger:Passenger, db:Session= Depends(get_db)):
#     db_passenger = Passengerdb(**passenger.model_dump())
#     db.add(db_passenger)
#     db.commit()
#     return db_passenger

# @app.get("/Passengers")
# def get_passenger(db:Session = Depends(get_db)):
#     passengers = db.query(Passengerdb).all()
#     return passengers

# @app.get("/Passengers/{id}")
# def get_passenger_by_id(id:int, db:Session = Depends(get_db)):
#     passenger = db.query(Passengerdb).filter(Passengerdb.id == id).first()
#     if passenger is None:
#         raise HTTPException(status_code=404, detail="Student not found")
#     return passenger

# @app.delete("/Passengers/{id}")
# def delete_passenger_by_id(id:int, db:Session = Depends(get_db)):
#     passenger = db.query(Passengerdb).filter(Passengerdb.id == id).first()
#     if passenger is None:
#         raise HTTPException(status_code=404, detail="Student not found")
#     db.delete(passenger)
#     db.commit()
#     return{"message": "Student deleted successfully"}

# @app.put("/Passengers/{id}")
# def update_patient_by_id(id:int,UpdatedPassenger:UpdatePassenger, db:Session = Depends(get_db)):
#     passenger = db.query(Passengerdb).filter(Passengerdb.id == id).first()
#     if passenger is None:
#         raise HTTPException(status_code=404, detail="Passenger not found")
#     update_data = UpdatedPassenger.model_dump(exclude_unset=True)
#     for field, value in update_data.items():
#         setattr(passenger, field, value)

#     db.commit()
#     db.refresh(passenger)
#     return passenger

    