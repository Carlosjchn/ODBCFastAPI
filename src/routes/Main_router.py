from fastapi import APIRouter, HTTPException
from ..database.Pruebas_bbdd import execute_query
from ..models.UserModel import User_Default_Response

router = APIRouter()

# Define routes using the router
@router.get("/users/", tags=["users"])
async def get_users() -> list:
    query = "SELECT u.* FROM usuario u "
    results = await execute_query(query)  # Pass id_usuario as a tuple
    if results is None:
        raise HTTPException(status_code=500, detail="Database query failed")
    return User_Default_Response(list(results))






