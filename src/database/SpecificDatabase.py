from .GeneralDatabase import GeneralMethods
from ..models.HorarioModel import Horario_Default_Response
from ..models.EquipoModel import Equipo_Default_Response
from .helpers.fetch.FetchUserHelper import (
    get_response_processor,
)



#########################
# Metodos para Usuarios #
#########################
class UserMethods(GeneralMethods):
    
    ############
    #  FETCHS  #
    ############
    
    @staticmethod
    async def fetch_user_data(query: str, horarios: bool = False, full_info: bool = False):
        # Ejecutar la consulta
        results = await GeneralMethods.execute_query_async(query)
        # Procesar y retornar la respuesta
        response_processor = get_response_processor(horarios, full_info)
        return response_processor(results)
            
    #############
    #  INSERTS  #
    #############
    
    @staticmethod
    async def insert_user(user_data):
        query = """
        INSERT INTO usuario (tipo, nombre, email, contrasena, id_equipo)
        VALUES (?, ?, ?, ?, ?)
        """
        
        await GeneralMethods.insert_data_async(query, user_data)
        return {"message": "User inserted successfully"}
    
        

    #############
    #  UPDATES  #
    #############
    @staticmethod
    async def update_user(query):
        await GeneralMethods.update_data_async(query)
        return {"message": "User updated successfully"}

    #############
    #  DELETES  #
    #############    
    @staticmethod
    async def delete_user(query):
        await GeneralMethods.delete_data_async(query)
        return {"message": "Usuario eliminado exitosamente"}

                   
                   
#########################
# Metodos para Horarios #
#########################
class HorariosMethods(GeneralMethods):
    
    ############
    #  FETCHS  #
    ############
    async def fetch_all_horarios():
        allHorarios = await GeneralMethods.execute_query_async(
            "SELECT h.* FROM horarios h"
        )
        return Horario_Default_Response(allHorarios)
    @staticmethod
    
    #############
    #  INSERTS  #
    #############
    async def insert_horario(horario_data):
        query = """
            INSERT INTO horarios (id_usuario, fecha, hora_inicio, hora_fin)
            VALUES (?, ?, ?, ?)
            """
        await GeneralMethods.insert_data_async(query, horario_data)
        return {"message": "Horario inserted successfully"}

    #############
    #  UPDATES  #
    #############
    @staticmethod
    async def update_horario(query):
        await GeneralMethods.update_data_async(query)
        return {"message": "Horario updated successfully"}
    
    #############
    #  DELETES  #
    ############# 
    @staticmethod
    async def delete_horario(horarioId):
        query = f"DELETE FROM horarios WHERE id_horario = {horarioId}"
        await GeneralMethods.delete_data_async(query)
        return {"message": "Horario deleted successfully"}
    
    
    
########################
# Metodos para Equipos #
########################
class EquiposMethods(GeneralMethods):
    
    ############
    #  FETCHS  #
    ############
    async def fetch_all_equipos():
        allEquipos = await GeneralMethods.execute_query_async(
            "SELECT e.* FROM equipos e"
        )
        return Equipo_Default_Response(allEquipos)
    
    #############
    #  INSERTS  #
    #############
    @staticmethod
    async def insert_equipo(equipo_data):
        query = """
        INSERT INTO equipos (tipo, nombre, horas_inicio_act, horas_fin_act)
        VALUES (?, ?, ?, ?)
        """
        await GeneralMethods.insert_data_async(query, equipo_data)
        return {"message": "Equipo inserted successfully"}

    #############
    #  UPDATES  #
    #############
    @staticmethod
    async def update_equipo(query):
        await GeneralMethods.update_data_async(query)
        return {"message": "Equipo updated successfully"}
    
    #############
    #  DELETES  #
    ############# 
    @staticmethod
    async def delete_equipo(equipoId):
        query = "DELETE FROM equipos WHERE id_equipo = {equipoId}"
        await GeneralMethods.delete_data_async(query)
        return {"message": "Equipo deleted successfully"}
