from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import jwt
from app.models import User
from app.schemas import UserCreate, Token
from app.database import get_db
from passlib.context import CryptContext

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")
router = APIRouter()

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
    

def create_access_token(data : dict):
    to_encode = data.copy()
    expire = datetime.utcnow()+ timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp" : expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)

@router.post("/register")
def register(user: UserCreate, db : Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    new_user = User(username = user.username, email = user.email, hashed_password = hashed_password)
    db.add(new_user)
    db.commit()
    return {"message": "User registered successfully!.." }

@router.post("/login", response_model=Token)
def login(user : UserCreate, db:Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token({"sub" : db_user.email})
    print(f"Access Token: {access_token}")
    return{"access_token" : access_token, "token_type": "bearer"}
