from .GeneralDatabase import GeneralMethods 
from ..models.UserModel import User_Default_Response, User_Details_Response
from ..models.HorarioModel import Horario_Default_Response
from ..models.EquipoModel import Equipo_Default_Response

class UserMethods(GeneralMethods):
      
    async def fetch_all_users():
        allUsers = await GeneralMethods.execute_query_async("SELECT u.* FROM usuario u")  # Await the result
        return User_Default_Response(allUsers)
    
    async def fetch_user_by_id(userId):
        User= await GeneralMethods.execute_query_async(f"SELECT u.* FROM usuario u WHERE u.id_usuario={userId}")
        return User_Default_Response(User)
    
    async def fetch_all_user_details():
        AllUsersDetails= await GeneralMethods.execute_query_async("SELECT u.*, h.* FROM usuario u JOIN horarios h ON u.id_usuario = h.id_usuario")
        return User_Details_Response(AllUsersDetails) 
    
    async def fetch_user_details_by_id(userId):
        UserDetails= await GeneralMethods.execute_query_async(f"SELECT u.*, h.* FROM usuario u JOIN horarios h ON u.id_usuario = h.id_usuario WHERE u.id_usuario={userId}")
        return User_Details_Response(UserDetails)

class HorariosMethods(GeneralMethods):
    async def fetch_all_horarios():
        allHorarios = await GeneralMethods.execute_query_async("SELECT h.* FROM horarios h")
        return Horario_Default_Response(allHorarios)
    
    
class EquiposMethods(GeneralMethods):
    async def fetch_all_equipos():
        allEquipos = await GeneralMethods.execute_query_async("SELECT e.* FROM equipos e")
        return Equipo_Default_Response(allEquipos)
    
    