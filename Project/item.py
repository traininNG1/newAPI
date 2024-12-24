from fastapi import APIRouter
 
router = APIRouter()

@router.get("/item")
def  get_items():
    return {"message" :  "items" }
