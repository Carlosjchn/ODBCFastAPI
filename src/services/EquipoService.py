from ..database.helpers.updater.UpdateEquipoHelper import build_update_equipo
from ..database.SpecificDatabase import EquiposMethods

###############
# Metodos Get #
###############
async def get_all_equipos_service():
    equipos = await EquiposMethods.fetch_all_equipos()
    return equipos

################
# Metodos Post #
################
async def insert_equipo_service(nombre_equipo: str,tipo: str, horas_inicio_act: str, horas_fin_act: str):
    equipo_data = (tipo,nombre_equipo,horas_inicio_act,horas_fin_act)         
    return await EquiposMethods.insert_equipo(equipo_data)

###############
# Metodos Put #
###############
async def update_equipo_service(id_equipo : int = None, id_usuario : int = None, fecha: str = None, hora_inicio: str = None, hora_fin: str = None):
    query = build_update_equipo(id_equipo, id_usuario, fecha, hora_inicio, hora_fin)
    return await EquiposMethods.update_equipo(query)

##################
# Metodos Delete #
##################
async def delete_equipo_service(id_equipo:int):
    return await EquiposMethods.delete_equipo(id_equipo)