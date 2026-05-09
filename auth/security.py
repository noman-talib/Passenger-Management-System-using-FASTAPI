from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])

def hashed_password(plain_password):
    hash_password = pwd_context.hash(plain_password)
    return hash_password

def verify_password(plain_password, hash_password):
    return pwd_context.verify(plain_password, hash_password)
    