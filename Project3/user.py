
from sqlalchemy import Column, String, Uuid
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    
    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True)
    age = Column(String)
    place = Column(String)
    email = Column(String, unique=True, index=True)
    
    # One-to-one relationship with Address
    address = relationship("Address", uselist=False, back_populates="parent", cascade="all, delete")
