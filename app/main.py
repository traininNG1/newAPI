from fastapi import FastAPI
from app.auth  import router as auth_router
from app.database import engine
from app.models import Base

app = FastAPI()

#creating db tables
Base.metadata.create_all(bind=engine)

app.include_router(auth_router, prefix="/auth", tags=["Authgentication"])

@app.get("/")
def root():
    return {"message" : "welcome to fastapi JWT Authentication"}

