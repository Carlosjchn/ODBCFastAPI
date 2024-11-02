from ..database.SpecificDatabase import EquiposMethods


async def get_all_equipos_service():
    equipos = await EquiposMethods.fetch_all_equipos()
    return equipos

async def insert_equipo_service(nombre_equipo: str, descripcion: str, horas_inicio_act: str, horas_fin_act: str):
    equipo_data = {
        "nombre_equipo": nombre_equipo,
        "descripcion": descripcion,
        "horas_inicio_act": horas_inicio_act,
        "horas_fin_act": horas_fin_act
    }
    
    if not equipo_data.get("nombre_equipo"):
        return {"error": "El nombre del equipo es requerido."}
    if not equipo_data.get("descripcion"):
        return {"error": "La descripción es requerida."}
    if not equipo_data.get("horas_inicio_act"):
        return {"error": "La hora de inicio de actividad es requerida."}
    if not equipo_data.get("horas_fin_act"):
        return {"error": "La hora de fin de actividad es requerida."}
    
    return await EquiposMethods.insert_equipo(equipo_data)