from fastapi import FastAPI
from enum import Enum
app = FastAPI()
class EnumFood(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    diary = "diary"

@app.get("/foods/{food_names}")
def get_food_list(food_name : EnumFood):
    if food_name.values == "vegetables":
        return  {
        "food_name":food_name, "message" :  "You r healthy"
        }
    
    if food_name.values == "fruits":
        return { 
            "food_name":food_name, "message" : "fruits is good for your health"
        }
    return{ "food_name":food_name, "message":"I like diary products"}

