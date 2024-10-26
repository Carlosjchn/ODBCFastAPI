from .GeneralDatabase import GeneralMethods 



class UserMethods(GeneralMethods):
      
    async def fetch_all_users():
        allUsers = await GeneralMethods.execute_query_async("SELECT u.* FROM usuario u")  # Await the result
        return allUsers
    
    async def fetch_user_by_id(userId):
        User= await GeneralMethods.execute_query_async(f"SELECT u.* FROM usuario u WHERE u.id_usuario={userId}")
        return User


class HorariosMethods(GeneralMethods):
    
    async def fetch_all_horarios():
        allUsers = await GeneralMethods.execute_query_async("SELECT h.* FROM horarios h")
        return allUsers