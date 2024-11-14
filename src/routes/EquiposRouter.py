from datetime import date, time
from fastapi import APIRouter, HTTPException, Query

from ..models.EquipoModel import Equipo
from ..services.EquipoService import (
    delete_equipo_service,
    get_all_equipos_service,
    insert_equipo_service,
    update_equipo_service,
)

router = APIRouter()


@router.get(
    "/all",
    summary="Obtener todos los equipos",
    responses={
        200: {
            "description": "Lista de equipos obtenida exitosamente.",
            "content": {
                "application/json": {
                    "example": {
                        "id_equipo": "int",
                        "tipo": "tipo_equipo",
                        "nombre": "nombre_equipo",
                        "horas_inicio_act": "HH:MM:SS",
                        "horas_fin_act": "HH:MM:SS",
                    }
                },
            },
        },
        500: {"description": "Error al obtener los equipos."},
    },
    response_model= list[Equipo]
)
async def get_all_equipos_router():
    """
    ---
    Endpoint para obtener todos los equipos registrados en la base de datos de manera asincrónica.

    ### Flujo del método:
    1. `get_all_equipos_router()` -> Llama al servicio para obtener todos los equipos.
    2. `get_all_equipos_service()` -> Construye la consulta para seleccionar todos los equipos y llama al repositorio para ejecutar la consulta en la base de datos.
    3. **EquipoMethods.**`get_all()` -> Ejecuta la consulta y devuelve los datos obtenidos.

    ### Returns:
    - Lista de todos los equipos registrados, incluyendo detalles de nombre, tipo y horas de actividad.
    """
    return await get_all_equipos_service()


@router.post(
    "/create",
    summary="Crear un nuevo equipo",
    responses={
        200: {"description": "Equipo creado exitosamente."},
        500: {"description": "Error al crear el equipo."},
    },
    response_model=dict,
)
async def create_equipo(
    nombre_equipo: str,
    tipo: str,
    hora_inicio_actividad: time = Query(
        ..., description="Hora de inicio del equipo (HH:MM:SS)"
    ),
    hora_fin_actividad: time = Query(
        ..., description="Hora de fin del equipo (HH:MM:SS)"
    ),
):
    """
    ---
    Endpoint para crear un nuevo equipo en la base de datos de manera asincrónica.

    ### Flujo del método:
    1. `create_equipo(nombre_equipo, tipo, hora_inicio_actividad, hora_fin_actividad)` -> Llama al servicio para crear un nuevo equipo.
    2. `insert_equipo_service(nombre_equipo, tipo, hora_inicio_actividad, hora_fin_actividad)` -> Construye la consulta de inserción y llama al repositorio para ejecutar la inserción en la base de datos.
    3. **EquipoMethods.**`insert()` -> Ejecuta la consulta de inserción y devuelve el resultado de la operación.

    ### Parámetros:
    - **nombre_equipo** (str): Nombre del equipo.
    - **tipo** (str): Tipo o categoría del equipo.
    - **hora_inicio_actividad** (time): Hora de inicio de actividades del equipo.
    - **hora_fin_actividad** (time): Hora de fin de actividades del equipo.

    ### Returns:
    - Un mensaje de confirmación indicando si la inserción fue exitosa o si hubo algún error.
    """
    return await insert_equipo_service(
        nombre_equipo, tipo, hora_inicio_actividad, hora_fin_actividad
    )


@router.put(
    "/update",
    summary="Actualizar un equipo existente",
    responses={
        200: {"description": "Equipo actualizado exitosamente."},
        404: {"description": "Equipo no encontrado."},
        500: {"description": "Error al actualizar el equipo."},
    },
)
async def update_equipo(
    id_equipo: int = None,
    tipo: str = None,
    nombre: str = None,
    hora_inicio_act: time = Query(
        None, description="Hora de inicio del equipo (HH:MM:SS)"
    ),
    hora_fin_act: time = Query(None, description="Hora de fin del equipo (HH:MM:SS)"),
):
    """
    ---
    Endpoint para actualizar un equipo existente en la base de datos de manera asincrónica.

    ### Flujo del método:
    1. `update_equipo(id_equipo, tipo, nombre, hora_inicio_act, hora_fin_act)` -> Llama al servicio para actualizar el equipo.
    2. `update_equipo_service(id_equipo, tipo, nombre, hora_inicio_act, hora_fin_act)` -> Construye la consulta de actualización y llama al repositorio para ejecutar la actualización en la base de datos.
    3. **EquipoMethods.**`update(query)` -> Ejecuta la consulta de actualización y devuelve el resultado de la operación.

    ### Parámetros:
    - **id_equipo** (int, opcional): ID del equipo a actualizar.
    - **tipo** (str, opcional): Nuevo tipo o categoría del equipo.
    - **nombre** (str, opcional): Nuevo nombre del equipo.
    - **hora_inicio_act** (time, opcional): Nueva hora de inicio de actividades del equipo.
    - **hora_fin_act** (time, opcional): Nueva hora de fin de actividades del equipo.

    ### Returns:
    - Resultado de la operación, indicando si la actualización fue exitosa o si hubo algún error.
    """
    return await update_equipo_service(
        id_equipo, tipo, nombre, hora_inicio_act, hora_fin_act
    )


@router.delete(
    "/delete",
    summary="Eliminar un equipo",
    responses={
        200: {"description": "Equipo eliminado exitosamente."},
        404: {"description": "Equipo no encontrado."},
        500: {"description": "Error al eliminar el equipo."},
    },
)
async def delete_equipo(id_equipo: int):
    """
    ---
    Endpoint para eliminar un equipo de la base de datos de manera asincrónica.

    ### Flujo del método:
    1. `delete_equipo(id_equipo)` -> Llama al servicio que elimina el equipo según el ID proporcionado.
    2. `delete_equipo_service(id_equipo)` -> Construye la consulta de eliminación y llama al repositorio para ejecutar la eliminación en la base de datos.
    3. **EquipoMethods.**`delete(id_equipo)` -> Ejecuta la consulta de eliminación y devuelve el resultado de la operación.

    ### Parámetros:
    - **id_equipo** (int): ID del equipo a eliminar.

    ### Returns:
    - Resultado de la operación, indicando si el equipo fue eliminado con éxito o si hubo algún error.
    """
    return await delete_equipo_service(id_equipo)
