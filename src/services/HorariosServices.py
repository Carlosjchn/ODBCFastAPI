from datetime import date, time

from ..database.helpers.updater.UpdateHorarioHelper import build_update_horario
from ..database.SpecificDatabase import HorariosMethods


###############
# Metodos Get #
###############
async def get_all_horarios_services():
    allHorarios = await HorariosMethods.fetch_all_horarios()
    return allHorarios

################
# Metodos Post #
################
async def insert_horario_service(id_usuario: int, fecha: date, hora_inicio: str, hora_fin: time):
    horario_data = (id_usuario, fecha, hora_inicio, hora_fin)
    # Llamada al método de la base de datos
    return await HorariosMethods.insert_horario(horario_data)

###############
# Metodos Put #
###############
async def update_horario_service(id_horario : int = None, id_usuario : int = None, fecha: str = None, hora_inicio: str = None, hora_fin: str = None):
    query = build_update_horario(id_horario, id_usuario, fecha, hora_inicio, hora_fin)
    return await HorariosMethods.update_horario(query)

##################
# Metodos Delete #
##################
async def delete_horario_service(id_horario:int):
    return await HorariosMethods.delete_horario(id_horario)