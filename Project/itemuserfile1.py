

from fastapi import FastAPI

#user.py file
from Router import user

#item.py file
from Router import item 



app = FastAPI()
#adding routers to the app
app.include_router(user.router)
app.include_router(item.router)

@app.get("/")
def read_root():
    return {"message" : "Welcome to fast api"}
