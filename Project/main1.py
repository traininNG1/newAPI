from shared import app
from user1 import  router as user_router
from item1 import router as item_router

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(item_router, prefix="/items", tags=["items"])