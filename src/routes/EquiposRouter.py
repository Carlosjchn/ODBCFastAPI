from datetime import date, time
from fastapi import APIRouter, HTTPException, Query

from ..services.EquipoService import get_all_equipos_service, insert_equipo_service, update_equipo_service

router = APIRouter()


@router.get("/all")
async def get_all_equipos_router():
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
    hora_inicio_actividad: time = Query(..., description="Hora de inicio del equipo (HH:MM:SS)"),
    hora_fin_actividad: time = Query(..., description="Hora de fin del equipo (HH:MM:SS)")
):
    """
    ---
    Endpoint para crear un nuevo equipo en la base de datos de manera asincrónica.

    ### Flujo del método:
    1. `create_equipo(nombre_equipo, descripcion, horas_inicio_act, horas_fin_act)` -> Llama al servicio que crea un nuevo equipo en la base de datos.
    2. `insert_equipo_service(nombre_equipo, descripcion, horas_inicio_act, horas_fin_act)` -> Procesa la solicitud y se comunica con la base de datos para insertar el equipo.
    3. **EquipoMethods.**`insert_equipo(equipo_data)` -> Inserta los datos en la base de datos.
    ---
    ### Parámetros:
    - **nombre_equipo** (str): Nombre del equipo.
    - **descripcion** (str): Descripción del equipo.
    - **horas_inicio_act** (str): Hora de inicio de actividades del equipo.
    - **horas_fin_act** (str): Hora de fin de actividades del equipo.
    ---
    ### Returns:
    - Un mensaje de confirmación indicando si la inserción fue exitosa o si hubo algún error.
    """
    return await insert_equipo_service(nombre_equipo, tipo, hora_inicio_actividad, hora_fin_actividad)

@router.put(
    "/update",
    summary="Actualizar un equipo existente",
    responses={
        200: {"description": "equipo actualizado exitosamente."},
        404: {"description": "equipo no encontrado."},
        500: {"description": "Error al actualizar el equipo."},
    },
)
async def update_equipo(
    id_equipo: int = None,
    tipo: str = None,
    nombre: str = None,
    hora_inicio_act: time = Query(None, description="Hora de inicio del equipo (HH:MM:SS)"),
    hora_fin_act: time = Query(None, description="Hora de fin del equipo (HH:MM:SS)")
):
    """
    Endpoint para actualizar un equipo existente en la base de datos de manera asincrónica.

    ### Parámetros:
    - **id_equipo** (int, opcional): ID del equipo a actualizar.
    - **id_usuario** (int, opcional): ID del usuario asociado al equipo.
    - **fecha** (str, opcional): Nueva fecha del equipo (YYYY-MM-DD).
    - **hora_inicio** (str, opcional): Nueva hora de inicio del equipo (HH:MM:SS).
    - **hora_fin** (str, opcional): Nueva hora de fin del equipo (HH:MM:SS).

    ### Returns:
    - Resultado de la operación, indicando éxito o algún error.
    """
    return await update_equipo_service(id_equipo, tipo, nombre, hora_inicio_act, hora_fin_act)

