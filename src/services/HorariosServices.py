from ..database.SpecificDatabase import HorariosMethods


async def get_all_horarios_services():
    allHorarios = await HorariosMethods.fetch_all_horarios()
    return allHorarios