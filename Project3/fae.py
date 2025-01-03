from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy.engine import URL
from pydantic import BaseModel
import uuid

app = FastAPI()

# Database configuration
url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="1234ABCD",
    host="localhost",
    database="cruddb",
    port=5432
)
engine = create_engine(url)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# SQLAlchemy Models
class User(Base):
    _tablename_ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True)
    age = Column(String, default="Unknown")
    place = Column(String, default="Unknown")
    email = Column(String, unique=True, index=True)

    # One-to-One relationship with Address
    address = relationship("Address", uselist=False, back_populates="parent", cascade="all, delete")


class Address(Base):
    _tablename_ = "address"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False)
    country = Column(String, index=True)
    street = Column(String, index=True)
    zip_code = Column(String, index=True)
    phone = Column(String, unique=True, index=True)

    # One-to-One relationship with User
    parent = relationship("User", back_populates="address")

Base.metadata.create_all(bind=engine)

# Pydantic Models
class AddressBase(BaseModel):
    country: str
    street: str
    zip_code: str
    phone: str

class AddressCreate(AddressBase):
    pass

class AddressResponse(AddressBase):
    id: uuid.UUID

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    age: str
    place: str
    email: str

class UserCreate(UserBase):
    address: AddressCreate

class UserResponse(UserBase):
    id: uuid.UUID
    address: AddressResponse

    class Config:
        orm_mode = True

# CRUD Operations
@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: SessionLocal = Depends(get_db)):
    db_user = User(
        name=user.name,
        age=user.age,
        place=user.place,
        email=user.email,
    )
    db_address = Address(
        country=user.address.country,
        street=user.address.street,
        zip_code=user.address.zip_code,
        phone=user.address.phone,
    )
    db_user.address = db_address

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: uuid.UUID, db: SessionLocal = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: uuid.UUID, user: UserCreate, db: SessionLocal = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    db_user.name = user.name
    db_user.age = user.age
    db_user.place = user.place
    db_user.email = user.email
    db_user.address.country = user.address.country
    db_user.address.street = user.address.street
    db_user.address.zip_code = user.address.zip_code
    db_user.address.phone = user.address.phone

    db.commit()
    db.refresh(db_user)
    return db_user

@app.delete("/users/{user_id}")
def delete_user(user_id: uuid.UUID, db: SessionLocal = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"detail": "User deleted"}

@app.get("/addresses/{address_id}", response_model=AddressResponse)
def get_address(address_id: uuid.UUID, db: SessionLocal = Depends(get_db)):
    address = db.query(Address).filter(Address.id == address_id).first()
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    return address
