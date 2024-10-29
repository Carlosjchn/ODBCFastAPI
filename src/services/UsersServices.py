from ..database.SpecificDatabase import UserMethods



async def get_all_users_service():
    allUsers = await UserMethods.fetch_all_users()
    return allUsers
    
async def get_user_byId_service(userId:int):
    user = await UserMethods.fetch_user_by_id(userId)
    return user

async def get_all_UserDetails_service():
    allUserDetails = await UserMethods.fetch_all_user_details()
    return allUserDetails

async def get_Details_byID_service(userId:int):
    userDetails = await UserMethods.fetch_user_details_by_id(userId)
    return userDetails

async def get_all_info_details_service():
    allInfoDetails = await UserMethods.fetch_all_info_details()
    return allInfoDetails