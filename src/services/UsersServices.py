from ..database.UsersDatabase import UserMethods
from ..models.UserModel import User_Default_Response


async def get_all_users_service():
    allUsers = await UserMethods.fetch_all_users()
    return User_Default_Response(allUsers)
    