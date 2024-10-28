from ..database.SpecificDatabase import UserMethods
from ..models.UserModel import User_Default_Response, User_Details_Response


async def get_all_users_service():
    allUsers = await UserMethods.fetch_all_users()
    return User_Default_Response(allUsers)
    
async def get_user_byId_service(userId:int):
    user = await UserMethods.fetch_user_by_id(userId)
    return User_Default_Response(user)

async def get_all_UserDetails_service():
    allUserDetails = await UserMethods.fetch_all_user_details()
    return User_Details_Response(allUserDetails)
