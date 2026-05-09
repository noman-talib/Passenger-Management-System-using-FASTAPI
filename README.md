# Passenger Management System — FastAPI

A Flight Management System with JWT Authentication 
and Role-Based Access Control (Admin/Passenger).

## Project Structure

Passenger-Management-System-using-FASTAPI/
│
├── auth/
│   ├── __init__.py
│   ├── security.py          # Password hashing
│   ├── jwt_handler.py       # JWT token create/decode
│   └── dependencies.py      # Route protection
│
├── models/
│   ├── __init__.py
│   ├── user.py              # User table
│   ├── flight.py            # Flight table
│   └── booking.py           # Booking table
│
├── schemas/
│   ├── __init__.py
│   ├── user.py              # User schemas
│   ├── flight.py            # Flight schemas
│   └── booking.py           # Booking schemas
│
├── controllers/
│   ├── __init__.py
│   ├── auth.py              # Register + Login logic
│   ├── flight.py            # Flight CRUD logic
│   └── booking.py           # Booking logic
│
├── routes/
│   ├── __init__.py
│   ├── auth.py              # /auth/register, /auth/login
│   ├── flights.py           # /flights/
│   └── bookings.py          # /bookings/
│
├── frontend/                # HTML/CSS/JS frontend
│
├── .env                     # Secret keys (not on GitHub)
├── .gitignore
├── db_connection.py         # Database connection
└── main.py                  # FastAPI app entry point

## Features
- JWT Authentication
- Role Based Access (Admin / Passenger)
- Admin: Add, Update, Delete Flights
- Passenger: View and Book Flights

## Tech Stack
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Python-Jose (JWT)
- Passlib (Bcrypt)

## Setup

1. Clone the repo
2. Create .env file:
   SECRET_KEY=your_secret_key
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   DATABASE_URL=sqlite:///./flightmanagementsystem.db

3. Install dependencies:
   pip install -r requirements.txt

4. Run the app:
   uvicorn main:app --reload