
from sqlalchemy import Column, String, Uuid, ForeignKey
from user import Base
from sqlalchemy.orm import relationship
import uuid 
#Base = declarative_base() 

class Address(Base):
    __tablename__ = "address"
    
    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    user_id = Column(Uuid, ForeignKey("user.id"), nullable=False)
    country = Column(String, index=True)
    street = Column(String, index=True)
    zip_code = Column(String, index=True)
    phone = Column(String, unique=True, index=True)
    
    # One-to-one relationship back to User
    parent = relationship("User", back_populates="address")
