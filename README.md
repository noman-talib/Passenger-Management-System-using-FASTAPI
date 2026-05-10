✈️ Flight Management System
A FastAPI-based Flight Management System with JWT Authentication
and Role-Based Access Control (Admin / Passenger).

📁 Project Structure
├── auth/
│   ├── security.py        # Password hashing
│   ├── jwt_handler.py     # JWT token create/decode
│   └── dependencies.py    # Route protection
│
├── models/
│   ├── user.py            # User table
│   ├── flight.py          # Flight table
│   └── booking.py         # Booking table
│
├── schemas/
│   ├── user.py            # User schemas
│   ├── flight.py          # Flight schemas
│   └── booking.py         # Booking schemas
│
├── controllers/
│   ├── auth.py            # Register + Login logic
│   ├── flight.py          # Flight CRUD logic
│   └── booking.py         # Booking logic
│
├── routes/
│   ├── auth.py            # /auth/register, /auth/login
│   ├── flights.py         # /flights/
│   └── bookings.py        # /bookings/
│
├── frontend/              # HTML/CSS/JS
├── db_connection.py       # Database connection
├── main.py                # Entry point
└── .env                   # Secret keys (not on GitHub)

✨ Features

🔐 JWT Authentication
👤 Role Based Access (Admin / Passenger)
✈️ Admin: Add, Update, Delete Flights
🎫 Passenger: View and Book Flights


🛠️ Tech Stack
TechnologyPurposeFastAPIBackend FrameworkSQLAlchemyORMSQLiteDatabasePydanticData ValidationPython-JoseJWT TokensPasslibPassword Hashing

🚀 Setup
1. Clone the repo
git clone https://github.com/noman-talib/Passenger-Management-System-using-FASTAPI.git
2. Create .env file
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./flightmanagementsystem.db
3. Install dependencies
pip install -r requirements.txt
4. Run the app
uvicorn main:app --reload
5. Open docs
http://127.0.0.1:8000/docs
