
from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str
    course: str

# Schema ....> creating a new student
class StudentCreate(StudentBase):
    status: bool = True 

# Schema .... student with additional details 
class Student(StudentBase):
    id: int
    status: bool
    courses: str

    class Config:
        orm_mode = True  


