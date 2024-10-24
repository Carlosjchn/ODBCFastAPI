from fastapi import APIRouter, HTTPException
from ..services.UsersServices import get_all_users_service



router = APIRouter()

# Define routes using the router
# @router.get("/users/", tags=["users"])
# async def get_users() -> list:
#     query = "SELECT u.* FROM usuario u "
#     results = await execute_query(query)  # Pass id_usuario as a tuple
#     if results is None:
#         raise HTTPException(status_code=500, detail="Database query failed")
#     return User_Default_Response(list(results))

@router.get("/all", tags=["All Users"])
async def get_all_users_router(): return await get_all_users_service()
 





