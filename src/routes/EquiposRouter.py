from fastapi import APIRouter, HTTPException

from ..services.EquipoService import get_all_equipos_service, insert_equipo_service

router = APIRouter()


@router.get("/all")
async def get_all_equipos_router():
    return await get_all_equipos_service()

@router.post(
    "/createEquipo",
    summary="Crear un nuevo equipo",
    responses={
        200: {"description": "Equipo creado exitosamente."},
        500: {"description": "Error al crear el equipo."},
    },
    response_model=dict,
)
async def create_equipo(
    nombre_equipo: str,
    descripcion: str,
    horas_inicio_act: str,
    horas_fin_act: str,
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
    return await insert_equipo_service(nombre_equipo, descripcion, horas_inicio_act, horas_fin_act)

