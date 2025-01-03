from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from user import Base

DATABASE_URL = "postgresql://postgres:1234ABCD@localhost/fastapi-db"  

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# This is used to create all the tables in the database.
Base.metadata.create_all(bind=engine)
