from fastapi import APIRouter

router = APIRouter()

# Define routes using the router
@router.get("/users/", tags=["users"])
def get_users():
    return {"users": ["user1", "user2"]}





