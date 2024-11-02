from datetime import date, time
from fastapi import APIRouter, Query
from ..services.HorariosServices import get_all_horarios_services, insert_horario_service

router2 = APIRouter()


@router2.get(path="/all", summary=" ")
async def get_all_horarios_router():
    return await get_all_horarios_services()

@router2.post(
    "/create",
    summary="Crear un nuevo horario",
    responses={
        200: {"description": "Horario creado exitosamente."},
        400: {"description": "Error en los datos enviados."},
        500: {"description": "Error al insertar el horario."},
    },
)
async def create_horario(
    id_usuario: int, 
    fecha: date = Query(..., description="Fecha del horario (YYYY-MM-DD)"),
    hora_inicio: time = Query(..., description="Hora de inicio del horario (HH:MM:SS)"),
    hora_fin: time = Query(..., description="Hora de fin del horario (HH:MM:SS)")
):
    """
    ---
    Endpoint para crear un nuevo horario en la base de datos de manera asincrónica.

    ### Parámetros:\n
    - **id_usuario** (int): ID del usuario asociado al horario.\n
    - **fecha** (str): Fecha del horario (YYYY-MM-DD).\n
    - **hora_inicio** (str): Hora de inicio del horario (HH:MM:SS).\n
    - **hora_fin** (str): Hora de fin del horario (HH:MM:SS).\n
    ---
    ### Returns:\n
    Resultado de la operación, indicando éxito o algún error.
    """
    return await insert_horario_service(id_usuario, fecha, hora_inicio, hora_fin)