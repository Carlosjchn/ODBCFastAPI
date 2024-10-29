from ..database.SpecificDatabase import EquiposMethods

async def get_all_equipos_service():
    equipos = await EquiposMethods.fetch_all_equipos()
    return equipos