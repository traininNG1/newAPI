# crud operation main  file

from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends

#from schemas import Config
import crud,models,schemas
#from models import models
from database import get_db
from fastapi import FastAPI


app = FastAPI()


# Create student
@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, student=student)

# Get all students
@app.get("/students/", response_model=list[schemas.Student])
def read_students(db: Session = Depends(get_db)):
    students = crud.get_students(db=db)
    return students

# Get a student ---> by ID
@app.get("/students/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db=db, student_id=student_id)
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

# Delete a student ---by ID
@app.delete("/students/{student_id}", response_model=schemas.Student)
def delete_student(student_id : int, db: Session = Depends(get_db)):
    return crud.delete_student(db = db, student_id = student_id) 

# JWT-AUTHORIZATION AND AUTHENTICATION


"""from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from jose import jwt, JWTError
from datetime import datetime, timedelta
from passlib.context import CryptContext

app = FastAPI()

# Configuration
SECRET_KEY = "keyy"
ALGORITHM = "HS256"
TOKEN_EXPIRE_MIN = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserLogin(BaseModel):
    username: str
    password: str

# creating a database
fake_db = {
    "user1": {
        "username": "user1",
        "hashed_password": pwd_context.hash("password1"),
    }
}


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(username: str, password: str):
    user = fake_db.get(username)
    if not user or not verify_password(password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )
    return user

def create_access_token(data: dict, expire_delta: timedelta = timedelta(minutes=TOKEN_EXPIRE_MIN)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expire_delta       #current time+ expiring tym
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)   #secret key = is used to sign the token...#algorithm = specifies the hashing algorithm used for signing the token.

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return username
    except JWTError:
        raise credentials_exception

# Routes creation
@app.post("/login")
def login(user: UserLogin):
    authenticate_user(user.username, user.password)
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/protected")
def read_protected(current_user: str = Depends(get_current_user)):
    return {"message": f"Hello {current_user}, this is a protected route!"}"""
#steps to run in postman
# step1: <url>/login -->run in post
#step2 : in the json body {"username" : "user1", "password": "password1"} 
# step3 : copy token and click on authorization and choose auth type as bearer token
# step 4: paste token and run -->get (here...<url>/protected)

# MIDDLEWARE
"""from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

class Simple_mw(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        print(f"Request URL : {request.url}")

        response = await call_next(request)
        print(f"Response status code : {response.status_code}") # logs the response status
        return response     #sends response back to the client


#adding middleware back to fastapi
app.add_middleware(Simple_mw)
@app.get("/")
def  read_root():
    return {"message" : "Hello, Welcome to Middleware"}"""


# CROS HANDLING
"""from fastapi import FastAPI
#from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://myfrontendapp.com",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins =["http://localhost:3000"],
    allow_credentials = True,
    allow_methods = ["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers = ["*"],
)

@app.get("/")
def read_root():
    return {"message" : "CROS - ENDPOINT ENABLED! "}"""