# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from user import Base, User
from address import Address
from schemauser import UserCreate, AddressCreate

# Create the tables in db
Base.metadata.create_all(bind=engine)
#Address.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the db session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint to create a new user
@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, age=user.age, place=user.place, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Endpoint to create an address for a user
@app.post("/addresses/")
def create_address(address: AddressCreate, user_id: str, db: Session = Depends(get_db)):
    db_address = Address(country=address.country, street=address.street, zip_code=address.zip_code, phone=address.phone, user_id=user_id)
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address
# files needed--> databaseuser.py, schemauser.py, address.py, user.py, mainuser.py