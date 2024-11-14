from datetime import date, time
from fastapi import APIRouter, Query
from ..services.HorariosServices import (
    get_all_horarios_services,
    insert_horario_service,
    update_horario_service,
    delete_horario_service
)

router2 = APIRouter()

@router2.get(path="/all", summary="Obtener todos los horarios")
async def get_all_horarios_router():
    """
    Endpoint para obtener todos los horarios registrados en la base de datos de manera asincrónica.
    """
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
    Endpoint para crear un nuevo horario en la base de datos de manera asincrónica.

    ### Parámetros:
    - **id_usuario** (int): ID del usuario asociado al horario.
    - **fecha** (str): Fecha del horario (YYYY-MM-DD).
    - **hora_inicio** (str): Hora de inicio del horario (HH:MM:SS).
    - **hora_fin** (str): Hora de fin del horario (HH:MM:SS).

    ### Returns:
    - Resultado de la operación, indicando éxito o algún error.
    """
    return await insert_horario_service(id_usuario, fecha, hora_inicio, hora_fin)

@router2.put(
    "/update",
    summary="Actualizar un horario existente",
    responses={
        200: {"description": "Horario actualizado exitosamente."},
        404: {"description": "Horario no encontrado."},
        500: {"description": "Error al actualizar el horario."},
    },
)
async def update_horario(
    id_horario: int = None,
    id_usuario: int = None,
    fecha: date = Query(None, description="Fecha del horario (YYYY-MM-DD)"),
    hora_inicio: time = Query(None, description="Hora de inicio del horario (HH:MM:SS)"),
    hora_fin: time = Query(None, description="Hora de fin del horario (HH:MM:SS)")
):
    """
    Endpoint para actualizar un horario existente en la base de datos de manera asincrónica.

    ### Parámetros:
    - **id_horario** (int, opcional): ID del horario a actualizar.
    - **id_usuario** (int, opcional): ID del usuario asociado al horario.
    - **fecha** (str, opcional): Nueva fecha del horario (YYYY-MM-DD).
    - **hora_inicio** (str, opcional): Nueva hora de inicio del horario (HH:MM:SS).
    - **hora_fin** (str, opcional): Nueva hora de fin del horario (HH:MM:SS).

    ### Returns:
    - Resultado de la operación, indicando éxito o algún error.
    """
    return await update_horario_service(id_horario, id_usuario, fecha, hora_inicio, hora_fin)

@router2.delete(
    "/delete",
    summary="Eliminar un horario",
    responses={
        200: {"description": "Horario eliminado exitosamente."},
        404: {"description": "Horario no encontrado."},
        500: {"description": "Error al eliminar el horario."},
    },
)
async def delete_horario(id_horario: int):
    """
    Endpoint para eliminar un horario de la base de datos de manera asincrónica.

    ### Parámetros:
    - **id_horario** (int): ID del horario a eliminar.

    ### Returns:
    - Resultado de la operación, indicando éxito o algún error.
    """
    return await delete_horario_service(id_horario)
