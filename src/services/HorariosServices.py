from ..database.SpecificDatabase import HorariosMethods
from ..models.HorarioModel import Horario_Default_Response

async def get_all_horarios_services():
    allHorarios = await HorariosMethods.fetch_all_horarios()
    return Horario_Default_Response(allHorarios)