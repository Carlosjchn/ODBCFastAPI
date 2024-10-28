from .GeneralDatabase import GeneralMethods 



class UserMethods(GeneralMethods):
      
    async def fetch_all_users():
        allUsers = await GeneralMethods.execute_query_async("SELECT u.* FROM usuario u")  # Await the result
        return allUsers
    
    async def fetch_user_by_id(userId):
        User= await GeneralMethods.execute_query_async(f"SELECT u.* FROM usuario u WHERE u.id_usuario={userId}")
        return User
    
    async def fetch_all_user_details():
        UserDetails= await GeneralMethods.execute_query_async("SELECT u.*, h.* FROM usuario u JOIN horarios h ON u.id_usuario = h.id_usuario")
        return UserDetails 


class HorariosMethods(GeneralMethods):
    async def fetch_all_horarios():
        allUsers = await GeneralMethods.execute_query_async("SELECT h.* FROM horarios h")
        return allUsers
    
    