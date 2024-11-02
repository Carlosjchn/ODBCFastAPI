from ..database.helpers.create.CreateUserHelper import validar_user_data
from ..database.helpers.delete.DeleteUserHelper import build_delete_query
from ..database.helpers.updater.UpdateUserHelper import build_update_query
from ..database.SpecificDatabase import UserMethods
from ..database.helpers.fetch.FetchUserHelper import query_builder

###############
# Metodos Get #
###############

async def get_user_data_services(
    userId: int = None, horarios: bool = False, full_info: bool = False
):

    query = query_builder(userId, horarios, full_info)

    users_data = await UserMethods.fetch_user_data(query, horarios, full_info)
    return users_data


################
# Metodos Post #
################

async def insert_user_service(
    tipo: str, nombre: str, email: str, password: str, id_equipo: int = None
):
    user_data = validar_user_data(tipo, nombre, email, password, id_equipo)
    return await UserMethods.insert_user(user_data)


###############
# Metodos Put #
###############
async def update_user_service(id_usuario: int, tipo: str = None, nombre: str = None, email: str = None, password: str = None, id_equipo: int = None):
    try:
        query, params = build_update_query(id_usuario, tipo, nombre, email, password, id_equipo)
        return await UserMethods.execute_update_query(query, params)
    except ValueError as e:
        return {"error": str(e)}

##################
# Metodos Delete #
##################
async def delete_user_service(id_usuario: int = None, nombre: str = None):
    query = build_delete_query(id_usuario, nombre)
    # Llamada al método de base de datos con los parámetros proporcionados
    return await UserMethods.delete_user(query)

