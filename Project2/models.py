from sqlalchemy import Column, Integer, String, Boolean
from database import Base




class Student(Base):
    __tablename__ = "student"  

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    course = Column(String, index=True)
    status = Column(Boolean)