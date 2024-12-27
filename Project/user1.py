from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_user():
    return {"message": "List of users"}