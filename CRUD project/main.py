from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "First FastAPI app"}

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="1234ABCD",
    host="localhost",
    database = "cruddb",
    port=5432
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    text = Column(String)
    is_done = Column(Boolean, default=False)

Base.metadata.create_all(engine)

@app.post("/create")
async def create_todo(text: str, is_complete: bool = False):
    todo = Todo(text=text, is_done=is_complete)
    session.add(todo)
    session.commit()
    return {"todo added": todo.text}