from datetime import date, time
from fastapi import APIRouter, Query

from ..models.HorarioModel import Horario
from ..services.HorariosServices import (
    get_all_horarios_services,
    insert_horario_service,
    update_horario_service,
    delete_horario_service,
)

router2 = APIRouter()


@router2.get(
    path="/all",
    summary="Obtener todos los horarios",
    responses={
        200: {
            "description": "Lista de horarios obtenida exitosamente.",
            "content": {
                "application/json": {
                    "example": {
                        "id_horario": "int",
                        "id_usuario": "int",
                        "fecha": "YYYY-MM-DD",
                        "hora_inicio": "HH:MM:SS",
                        "hora_fin": "HH:MM:SS",
                    }
                },
            },
        },
        500: {"description": "Error al obtener los horarios."},
    },
    response_model=list[Horario],
)
async def get_all_horarios_router():
    """
    ---
    Endpoint para obtener todos los horarios registrados en la base de datos de manera asincrónica.

    ### Flujo del método:
    1. `get_all_horarios_router()` -> Llama al servicio que obtiene todos los horarios.\n
    2. `get_all_horarios_services()` -> Crea la query para obtener todos los horarios y llama al repositorio para realizar la consulta en la base de datos.\n
    3. **HorariosMethods.**`get_all_horarios(query)` -> Ejecuta la query y devuelve los horarios desde la base de datos.\n
    ---
    ### Returns:
    - Lista de todos los horarios registrados, incluyendo detalles de fecha y horas.
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
    hora_fin: time = Query(..., description="Hora de fin del horario (HH:MM:SS)"),
):
    """
    ---
    Endpoint para crear un nuevo horario en la base de datos de manera asincrónica.

    ### Flujo del método:
    1. `create_horario(id_usuario, fecha, hora_inicio, hora_fin)` -> Llama al servicio para crear el nuevo horario.\n
    2. `insert_horario_service(id_usuario, fecha, hora_inicio, hora_fin)` -> Crea la query de inserción para el horario y llama al repositorio para insertar el registro en la base de datos.\n
    3. **HorariosMethods.**`insert_horario(query)` -> Ejecuta la query para insertar el horario en la base de datos.\n
    ---
    ### Parámetros:
    - **id_usuario** (int): ID del usuario asociado al horario.
    - **fecha** (date): Fecha del horario en formato (YYYY-MM-DD).
    - **hora_inicio** (time): Hora de inicio del horario en formato (HH:MM:SS).
    - **hora_fin** (time): Hora de fin del horario en formato (HH:MM:SS).
    ---
    ### Returns:
    Resultado de la operación, indicando si la creación del horario fue exitosa o si hubo algún error.
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
    hora_inicio: time = Query(
        None, description="Hora de inicio del horario (HH:MM:SS)"
    ),
    hora_fin: time = Query(None, description="Hora de fin del horario (HH:MM:SS)"),
):
    """
    ---
    Endpoint para actualizar un horario existente en la base de datos de manera asincrónica.

    ### Flujo del método:
    1. `update_horario(id_horario, id_usuario, fecha, hora_inicio, hora_fin)` -> Llama al servicio para actualizar el horario.\n
    2. `update_horario_service(id_horario, id_usuario, fecha, hora_inicio, hora_fin)` -> Crea la query de actualización para el horario y llama al repositorio para ejecutar la actualización en la base de datos.\n
    3. **HorariosMethods.**`update_horario(query)` -> Ejecuta la query de actualización en la base de datos.\n
    ---
    ### Parámetros:
    - **id_horario** (int, opcional): ID del horario a actualizar.
    - **id_usuario** (int, opcional): ID del usuario asociado al horario.
    - **fecha** (date, opcional): Nueva fecha del horario (YYYY-MM-DD).
    - **hora_inicio** (time, opcional): Nueva hora de inicio del horario (HH:MM:SS).
    - **hora_fin** (time, opcional): Nueva hora de fin del horario (HH:MM:SS).
    ---
    ### Returns:
    Resultado de la operación, indicando si la actualización fue exitosa o si hubo algún error.
    """
    return await update_horario_service(
        id_horario, id_usuario, fecha, hora_inicio, hora_fin
    )


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
    ---
    Endpoint para eliminar un horario de la base de datos de manera asincrónica.

    ### Flujo del método:
    1. `delete_horario(id_horario)` -> Llama al servicio que elimina el horario según el ID proporcionado.\n
    2. `delete_horario_service(id_horario)` -> Crea la query de eliminación y llama al repositorio para ejecutar la eliminación en la base de datos.\n
    3. **HorariosMethods.**`delete_horario(query)` -> Ejecuta la query de eliminación en la base de datos.\n
    ---
    ### Parámetros:
    - **id_horario** (int): ID del horario que se desea eliminar.
    ---
    ### Returns:
    Resultado de la operación, indicando si el horario fue eliminado con éxito o si hubo algún error.
    """
    return await delete_horario_service(id_horario)
