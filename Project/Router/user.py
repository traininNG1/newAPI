
from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/users")
def get_user():
    return [ {"id": 1, "name": "haris"},{"id":2, "name": "rea"}]
@router.get("/{user_id}")
def get_user(user_id : int):
    return { "id":user_id, "name": f"user{user_id}"}