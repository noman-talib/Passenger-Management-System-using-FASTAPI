from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from db_connection import get_db
from jwt_handler import decode_token
from models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
):
    payload = decode_token(token)
    user_id = payload.get("sub")
    user = db.query(User).filter(User.id == int(user_id)).first()

    if not user:
        raise HTTPException(status_code= 401, detail="User not found")
    return user

def require_admin(current_user = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code= 403, detail="It requires admin")
    return current_user

def require_user(current_user = Depends(get_current_user)):
    if current_user.role != "passenger":
        raise HTTPException(status_code= 403, detail="It requires Passenger")
    return current_user