# crud operation main  file

from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends

""" from schemas import Config """
from . import crud,models,schemas
from models import models
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
