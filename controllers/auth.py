from fastapi import HTTPException, Depends
from db_connection import get_db
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate, UserLogin, UserResponse
from auth.security import hashed_password, verify_password
from auth.jwt_handler import create_token
from schemas.booking import TokenResponse

def register(user_data: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email Already Exists")
    password = hashed_password(user_data.password)
    new_user = User(
        name = user_data.name,
        email = user_data.email,
        password = password,
        age = user_data.age,
        gender = user_data.gender,
        cnic = user_data.cnic,
        phone_number = user_data.phone_number,
        role = user_data.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def login(user_data: UserLogin, db:Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    is_valid = verify_password(user_data.password, existing_user.password)
    if not is_valid:
        raise HTTPException(status_code=401, detail="Invalid Password")
    
    token = create_token(existing_user.id, existing_user.role)

    return TokenResponse(
        access_token=token,
        token_type="bearer"
    )