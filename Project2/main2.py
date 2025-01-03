#request and response validation with Pydantic

""" from fastapi import FastAPI,HTTPException
from pydantic  import BaseModel, Field


app = FastAPI()

# rqst model
class Item(BaseModel):
    name : str = Field(..., max_length=100, description="name of the item")
    price : float = Field(..., ge=2, description="price of the item")
    is_offer : bool = Field(default=False, description="offer item")

#response model
class Response(BaseModel):
    success : bool
    data : Item
    message : str

@app.post("/items", response_model= Response)
def create_item(item: Item):
    if item.price > 1000:
        raise HTTPException(status_code=400, details= " price too high")
    return Response(success=True, data=item, message="item created successfully")

@app.get("/items/sample", response_model=Item)
def sample_item():
    sample_item = Item(name="sample", price=100.20, is_offer=True) """

""" # JWT
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from jose import jwt, JWTError
from datetime import datetime, timedelta
from passlib.context import CryptContext

app = FastAPI()

SECRET_KEY = "key"
ALGORITHM = "HS256"  
TOKEN_EXPIRE_MIN = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserLogin(BaseModel):
    username: str
    password: str

fake_db = {
    "user1": {
        "username": "jeevva",
        "hashed_password": pwd_context.hash("123abc"),
    }
}
def verify_pass(p_password, hashed_password):
    return pwd_context.verify(p_password, hashed_password)

def authenticate_user(username: str, password: str):
    user = fake_db.get(username)
    if not user or not verify_pass(password, user["hashed_password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return user

def create_access_token(data: dict, expire_delta: timedelta = timedelta(minutes=TOKEN_EXPIRE_MIN)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expire_delta    #current time+ expiring tym
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)     #secret key = is used to sign the token...#algorithm = specifies the hashing algorithm used for signing the token.

    return encoded_jwt

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
    except jwt.PyJWTError:
        raise credentials_exception

@app.post("/login")
def login(user: UserLogin):
    user_data = authenticate_user(user.username, user.password)
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/protected")
def read_protected(current_user: str = Depends(get_current_user)):
    return {"message": f"Hello {current_user}, this is a protected route!"}"""





