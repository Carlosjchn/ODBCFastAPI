from ..database.SpecificDatabase import HorariosMethods


async def get_all_horarios_services():
    allHorarios = await HorariosMethods.fetch_all_horarios()
    return allHorarios

async def insert_horario_service(id_usuario: int, fecha: str, hora_inicio: str, hora_fin: str):
    horario_data = {
        "id_usuario": id_usuario,
        "fecha": fecha,
        "hora_inicio": hora_inicio,
        "hora_fin": hora_fin,
    }
    
    # Validación de parámetros
    if not horario_data.get("id_usuario"):
        return {"error": "El ID de usuario es requerido."}
    if not horario_data.get("fecha"):
        return {"error": "La fecha es requerida."}
    if not horario_data.get("hora_inicio"):
        return {"error": "La hora de inicio es requerida."}
    if not horario_data.get("hora_fin"):
        return {"error": "La hora de fin es requerida."}

    # Llamada al método de la base de datos
    return await HorariosMethods.insert_horario(horario_data)