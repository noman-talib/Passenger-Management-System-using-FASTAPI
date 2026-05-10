from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from db_connection import get_db
from controllers.auth import register, login
from schemas.user import UserCreate, UserLogin,UserResponse
from schemas.booking import TokenResponse

router = APIRouter(
    prefix="/auth",
    tags=["Auth"] 
)

@router.post("/register", response_model = UserResponse)
def register_user(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    return register(user_data,db)

@router.post("/login", response_model = TokenResponse)
def login_user(
    user_data : UserLogin,
    db :Session = Depends(get_db)
):
    return login(user_data, db)