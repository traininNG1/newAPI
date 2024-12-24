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
