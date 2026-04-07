# 🚌 Passenger Management System using FastAPI

A full stack CRUD web application for managing passenger records, built with **FastAPI**, **SQLAlchemy**, and vanilla **HTML, CSS & JavaScript**.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | FastAPI |
| **ORM** | SQLAlchemy |
| **Database** | SQLite (passengers.db) |
| **Middleware** | CORS Middleware |
| **Frontend** | HTML, CSS, JavaScript |
| **API Communication** | Fetch API (Promises) |
| **DOM Manipulation** | Vanilla JS |

---

## 📁 Project Structure

```
Passenger-Management-System-using-FASTAPI/
│
├── frontend/
│   ├── index.html            # Home page
│   ├── addPassenger.html     # Add new passenger form
│   ├── getAll.html           # View all passengers
│   ├── getbyid.html          # Get passenger by ID
│   ├── update.html           # Update passenger form
│   ├── delete.html           # Delete passenger
│   ├── style.css             # Styling
│   ├── add.js                # JS for adding passenger
│   ├── first.js              # Entry JS logic
│   ├── getall.js             # JS for fetching all passengers
│   ├── getbyid.js            # JS for fetching by ID
│   ├── update.js             # JS for updating passenger
│   └── delete.js             # JS for deleting passenger
│
├── main.py                   # FastAPI app & API routes
├── db_connection.py          # SQLAlchemy engine & session
├── passenger.py              # SQLAlchemy model
├── schemas.py                # Pydantic schemas
└── passengers.db             # SQLite database file
```

---

## ✨ Features

- ✅ **Add** a new passenger
- ✅ **View** all passengers
- ✅ **Search** passenger by ID
- ✅ **Update** passenger details
- ✅ **Delete** a passenger record
- ✅ **CORS Middleware** for frontend-backend communication
- ✅ **DOM Manipulation** to dynamically render data
- ✅ **Promises** via Fetch API for async API calls

---

## 🗄️ Database Model

```python
class Passenger(Base):
    __tablename__ = "passengers"

    id           = Column(Integer, primary_key=True)
    name         = Column(String)
    cnic         = Column(String)
    age          = Column(Integer)
    gender       = Column(String)
    destination  = Column(String)
    fare         = Column(Integer)
    phone_number = Column(Integer)
```

| Field | Type | Description |
|---|---|---|
| `id` | Integer (PK) | Auto-generated ID |
| `name` | String | Passenger full name |
| `cnic` | String | National ID card number |
| `age` | Integer | Passenger age |
| `gender` | String | Gender |
| `destination` | String | Travel destination |
| `fare` | Integer | Ticket fare |
| `phone_number` | Integer | Contact number |

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/passengers` | Get all passengers |
| `GET` | `/passengers/{id}` | Get a passenger by ID |
| `POST` | `/passengers` | Add a new passenger |
| `PUT` | `/passengers/{id}` | Update passenger details |
| `DELETE` | `/passengers/{id}` | Delete a passenger |

---

## ⚙️ Middleware

- **CORSMiddleware** — Allows the HTML/JS frontend to make requests to the FastAPI backend without cross-origin errors

---

## 🌐 Frontend Concepts Used

### DOM Manipulation
- Dynamically rendering passenger data into HTML tables
- Handling form submissions without page reload
- Showing success/error messages on the page

### Promises (Fetch API)
- All API calls use `fetch()` which returns Promises
- `.then()` and `.catch()` handle success and error responses
- Async/Await for cleaner asynchronous code flow

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/Passenger-Management-System-using-FASTAPI.git
cd Passenger-Management-System-using-FASTAPI
```

### 2. Install dependencies
```bash
pip install fastapi uvicorn sqlalchemy
```

### 3. Run the FastAPI server
```bash
uvicorn main:app --reload
```

### 4. Open the frontend
Open `frontend/index.html` in your browser or use the Live Server extension in VS Code.

> Make sure the backend is running on `http://127.0.0.1:8000` before opening the frontend.

### 5. Explore the API docs
FastAPI provides built-in interactive docs at:
```
http://127.0.0.1:8000/docs
```

---

## 📚 What I Learned

- Building REST APIs with **FastAPI**
- Defining database models with **SQLAlchemy ORM**
- Using **CORS Middleware** for frontend-backend communication
- Connecting a vanilla JS frontend to a Python backend
- Handling async operations using **Promises** and **Fetch API**
- Dynamically updating the UI using **DOM Manipulation**

---

## 🙋‍♂️ Author

**Noman Talib**
- GitHub: [@noman-talib](https://github.com/noman-talib)

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
