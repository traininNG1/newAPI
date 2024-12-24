

from fastapi import FastAPI

#user.py file
from user import router as user_router

#item.py file
from item import router as item_router



app = FastAPI()
#adding routers to the app
app.include_router(user_router)
app.include_router(item_router)
