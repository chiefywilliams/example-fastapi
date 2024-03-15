from passlib.context import CryptContext
#passlib seems to be abandoned and the new bcrypt doesn't work with it. Needs to force bcrypt==4.0.1 to keep using passlib
#otherwise continues to work, but get error displayed!

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)