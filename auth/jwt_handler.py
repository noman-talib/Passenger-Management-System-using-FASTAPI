from jose import jwt, JWTError
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
from fastapi import HTTPException


load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

def create_token(user_id, role):
    data = {
  "sub": str(user_id),
  "role": role,
  "exp": datetime.utcnow() + timedelta(minutes = 30)
}
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token

def decode_token(token):
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return data
    except JWTError:
        raise HTTPException(status_code=401, detail="Token invalid and expired")