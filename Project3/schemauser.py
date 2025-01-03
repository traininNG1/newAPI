
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    age: str
    place: str
    email: str

class AddressCreate(BaseModel):
    country: str
    street: str
    zip_code: str
    phone: str
