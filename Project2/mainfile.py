from fastapi import FastAPI,Query,Path
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

""" 
@app.get("/items/{item_id}")
def get_item(item_id: str, q:str | None = None):
    if q:
        return{"item_id":item_id, "q":q}
    return{"item_id":item_id}
 """

#( shift+alt + A...for comment)
#que using boolean
""" @app.get("/items/{item_id}")
def get_item13(item_id:str, q: str |  None = None, short: bool=False):
    item = {"item_id" : item_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update(
            {
                "description": "Welcome to the world of Fastapi...."
            }
        )
        return item """


#nxt que
""" @app.get("/users/{user_id}/items/{item_id}")
def get_user_item(user_id : int, item_id: str, q:str | None = None, short: bool=False):
    item = {"item_id": item_id, "user_id": user_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update({"description":"no q here..."})

        return item """

#nxt que
#import pydantic and typing

""" class Item(BaseModel):
    name : str
    description : str | None = None
    price : float
    tax : float | None = None

@app.post("/items")
def item_list51(item: Item):
    return item """ 

#adding price
""" class Item(BaseModel):
    name : str
    description : str | None = None
    price : float
    tax : float | None = None """

""" @app.post('/items')
def item62(item : Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price of item": price_with_tax})
    return item_dict

@app.put("/items/{item_id}")
def create_item71(item_id : int, item:Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result """

#eg for Query parameters

""" class Item(BaseModel):
    name : str
    description : str | None = None
    price : float
    tax : float | None = None


@app.get('/items')
def items78(q: list[str] | None =  Query(None)): # for this import Query in: --> from fastapi import FastAPI, Query
    results = {"items": [{"item_id": "foo"}, {"item_id": "zoo"} ]}
    if q:
        results.update({"q": q})
    return results """

   #string validation

"""@app.get("/items")
def items94(name : str = Query(...,min_length=3,max_length=15,regex="^[a-zA-Z0-9]+$"), description : str = Query(None, max_length=100)):
    return {"name" : name, "description" : description}
 """

    # BASIC PATH PARAMETER
""" @app.get("/items/{item_id}")    # item_id is the path parameter
def  get_list102(item_id : int):
    return {"item_id" : item_id}    """

    # PATH PARAMETERS WITH NUMERIC VALIDATION
# import path in --> from fastapi import FastAPI, Path
""" 
@app.get("/items/{item_id}")
def get_items109(item_id : int = Path(..., title="ID of the items",description="All item id are listed here", ge=2, le=200)):
    return { "item_id" : item_id}
 """
# combining path parametr with query parameter
""" @app.get("/items/{item_id}")
def get_list_user114(item_id : int = Path(...,title = "id proof", ge=1), 
size : int = Query(10,title="main list", le=300)):
    return { "item_id": item_id, "Size" : size} """


# custom validation with regular expression
""" @app.get("/users/{user_id}")
def userlist121(user_id : str =Path(..., regex="^[A-Z0-9]{7}$")):
    return {"User_id" : user_id} """


# simple request body ( video 7)
# need to import FastAPI & BaseModel

class Offer(BaseModel):
    name : str
    price : float
    is_offer : bool = False

@app.post("/items")
def offer134(item:  Offer):
    return {"item" : item} 

# ex2 MIXING PATH, QUERY & BODY PARAMETERS
# here import FastAPI & BaseModel


class Purchase(BaseModel):
    name : str
    price : float

@app.put("/items/{item_id}")
def item146(item : Purchase, item_id : int, q : str | None=None):
    return{
        "itemid": item_id, "item": item , "query":  q
    }

# MULTIPLE REQUEST BODIES
# here import FastAPI & BaseModel

class User(BaseModel):
    name : str
    email : str
    address : str

class Order(BaseModel):
    item_name : str
    quantity : int

@app.post("/users/{user_id}")
def user164( user_details : User, oredr_details : Order):
    return{"user details": user_details, "order details": oredr_details}

