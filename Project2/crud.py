from sqlalchemy.orm import Session
from . import models, schemas

def get_student(db: Session, student_id: int):

    # Retrieve a single student by ID
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def get_students_by_name(db: Session, name: str):
    return db.query(models.Student).filter(models.Student.name == name).all()       #Retrieve students by name.

def get_students(db: Session):
    return db.query(models.Student).all()       #Retrieve all students.
        
    

def create_student(db: Session, student: schemas.StudentCreate):

        #Create a new student.
    db_student = models.Student(
        name=student.name,
        course=student.course,
        status=student.status
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
