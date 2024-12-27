from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.put("/")
def put():
    return {"Message": "Hello frm the put route"}

@app.get("/users")
def users_list():
    return {"message": "List of users"}

@app.get("/users/{user_id}")
def users_list(user_id: str):
    return {"user_lisidt" :user_id}

from enum import Enum
class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    diary = "diary"

@app.get("/foods/{food_name}")
def get_food(food_name : FoodEnum):
    if food_name == FoodEnum.vegetables:
        return  {
        "food_name":food_name, "message" :  "You r healthy"
        }
    
    if food_name.value == "fruits":
        return { 
            "food_name":food_name, "message" : "fruits is good for your health"
        }
    return{ "food_name":food_name, "message": "I like diary products"}

#another que
fake_db = [{"item_name": "zoho"}, {"item_name": "bar"}, {"item_name": "jazz"}, {"item_name": "star"}]

@app.get("/items")
def list_items(skip: int=0, limit: int = 10):
    return fake_db[skip: skip+limit]

#nxt que
@app.get("/items/{item_id}")
def get_item49(item_id : str, q: str | None = None):
    if q:
        return{"item_id":item_id, "q":q}
    return{"item_id" : item_id}
