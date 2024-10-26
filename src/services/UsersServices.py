from ..database.SpecificDatabase import UserMethods
from ..models.UserModel import User_Default_Response


async def get_all_users_service():
    allUsers = await UserMethods.fetch_all_users()
    return User_Default_Response(allUsers)
    
async def get_user_byId_service(userId:int):
    user = await UserMethods.fetch_user_by_id(userId)
    return User_Default_Response(user)