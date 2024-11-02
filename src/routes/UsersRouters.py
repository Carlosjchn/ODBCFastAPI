from typing import Union
from fastapi import APIRouter, HTTPException
from ..services.UsersServices import (
    delete_user_service,
    get_user_data_services,
    insert_user_service,
    update_user_service,
)
from ..models.UserModel import User, UserDetails, UserBasicDetails


router = APIRouter()


@router.get(
    "/getUserData",
    summary="Obtener información global de usuarios con opciones de filtrado",
    responses={
        200: {
            "description": "Operación exitosa.",
            "content": {
                "application/json": {
                    "examples": {
                        "usuario": {
                            "summary": "Ejemplo de un usuario",
                            "value": {
                                "id_usuario": "int",
                                "tipo": "tipo",
                                "nombre": "nombre_usuario",
                                "email": "correo_usuario@gmail.com",
                                "password": "contraseña123",
                                "id_equipo": "int",
                            },
                        },
                        "detalles_usuario": {
                            "summary": "Ejemplo de un usuario con detalles",
                            "value": [
                                {
                                    "id_usuario": "int",
                                    "tipo": "tipo",
                                    "nombre": "nombre_usuario",
                                    "email": "correo_usuario@gmail.com",
                                    "password": "contraseña123",
                                    "id_equipo": "int",
                                    "horarios": [
                                        {
                                            "id_horario": "int",
                                            "fecha": "YYYY-MM-DD",
                                            "hora_inicio": "HH:MM:SS",
                                            "hora_fin": "HH:MM:SS",
                                        }
                                    ],
                                }
                            ],
                        },
                        "informacion_global": {
                            "summary": "Ejemplo de información global de un usuario",
                            "value": [
                                {
                                    "id_usuario": "int",
                                    "tipo": "tipo",
                                    "nombre": "nombre_usuario",
                                    "email": "correo_usuario@gmail.com",
                                    "password": "contraseña123",
                                    "id_equipo": "int",
                                    "equipo": [
                                        {
                                            "id_equipo": "int",
                                            "tipo": "tipo_equipo",
                                            "nombre": "nombre_equipo",
                                            "horas_inicio_act": "HH:MM:SS",
                                            "horas_fin_act": "HH:MM:SS",
                                        }
                                    ],
                                    "horarios": [
                                        {
                                            "id_horario": "int",
                                            "fecha": "YYYY-MM-DD",
                                            "hora_inicio": "HH:MM:SS",
                                            "hora_fin": "HH:MM:SS",
                                        }
                                    ],
                                }
                            ],
                        },
                    }
                }
            },
        },
        404: {"description": "No se encontraron datos."},
        500: {"description": "Error ejecutando la consulta."},
    },
    response_model=Union[list[User], list[UserBasicDetails], list[UserDetails]],
)
async def get_user_data_router(
    userId: int = None, horarios: bool = False, full_info: bool = False
):
    """
    ---
    Método para obtener información global de usuarios en la base de datos de manera asincrónica.

    # Flujo del método:\n
    1. `get_user_data_router(userId, horarios, full_info)` -> Llama al servicio que obtiene la información de usuario según los parámetros proporcionados.\n
    2. `get_user_data_services(userId, horarios, full_info)` -> Procesa la solicitud y se comunica con los métodos de la base de datos.\n
    3. **UserMethods.**`fetch_user_data(userId, horarios, full_info)` -> Procesa la solicitud y se comunica con los métodos de la base de datos.\n
    ---
    ### Parámetros:\n
    - **userId** (int, optional): ID del usuario a obtener. Si es None, obtiene todos los usuarios.\n
    - **horarios** (bool, optional): Si es True, incluye detalles de horarios en la consulta.\n
    - **full_info** (bool, optional): Si es True, incluye detalles de horarios y equipos en la consulta.\n
    ---
    ### Returns:\n
    Lista de usuarios con su información global, que incluye:\n
    - Información básica de usuario.\n
    - Detalles de equipo asociados, si existen.\n
    - Información de horarios asignados, si están disponibles.
    """
    return await get_user_data_services(userId, horarios, full_info)


@router.post(
    "/create",
    summary="Crear un nuevo usuario en la base de datos",
    responses={
        200: {"description": "Usuario creado exitosamente."},
        400: {"description": "Datos no válidos para crear el usuario."},
        500: {"description": "Error al crear el usuario."},
    },
)
async def create_user(
    tipo: str, nombre: str, email: str, password: str, id_equipo: int = None
):
    """
    ---
    Endpoint para crear un nuevo usuario en la base de datos de manera asincrónica.

    # Flujo del método:\n
    1. `create_user(tipo, nombre, email, password, id_equipo)` -> Llama al servicio que crea un nuevo usuario en la base de datos.\n
    2. `insert_user_service(tipo, nombre, email, password, id_equipo)` -> Procesa la solicitud y se comunica con los métodos de la base de datos para insertar el nuevo usuario.\n
    3. **UserMethods.**`insert_user(user_data)` -> Procesa la solicitud y ejecuta la consulta para insertar el usuario en la base de datos.\n
    ---
    ### Parámetros:\n
    - **tipo** (str): Tipo de usuario que se va a crear.\n
    - **nombre** (str): Nombre del nuevo usuario.\n
    - **email** (str): Correo electrónico del nuevo usuario.\n
    - **password** (str): Contraseña del nuevo usuario.\n
    - **id_equipo** (int, optional): ID del equipo al que el usuario estará asociado (si aplica).\n
    ---
    ### Returns:\n
    Resultado de la operación, que indica si la creación del usuario fue exitosa o si hubo algún error.
    """
    return await insert_user_service(tipo, nombre, email, password, id_equipo)


@router.delete(
    "/delete",
    summary="Eliminar un usuario por su ID o nombre",
    responses={
        200: {"description": "Usuario eliminado exitosamente."},
        400: {"description": "ID de usuario o nombre no válido."},
        404: {"description": "Usuario no encontrado."},
        500: {"description": "Error al eliminar el usuario."},
    },
)
async def delete_user_router(id_usuario: int = None, nombre: str = None):
    """
    ---
    Endpoint para eliminar un usuario de la base de datos de manera asincrónica.

    # Flujo del método:\n
    1. `delete_user_router(id_usuario, nombre)` -> Llama al servicio que elimina al usuario según el ID o nombre proporcionado.\n
    2. `delete_user_service(id_usuario, nombre)` -> Procesa la solicitud y se comunica con los métodos de la base de datos para eliminar al usuario.\n
    3. **UserMethods.**`delete_user(id_usuario, nombre)` -> Ejecuta la consulta de eliminación en la base de datos.\n
    ---
    ### Parámetros:\n
    - **id_usuario** (int, optional): ID del usuario que se desea eliminar.\n
    - **nombre** (str, optional): Nombre del usuario que se desea eliminar.\n
    ---
    ### Returns:\n
    Resultado de la operación, indicando si el usuario fue eliminado con éxito o si hubo algún error.
    """
    return await delete_user_service(id_usuario, nombre)


@router.put(
    "/update",
    summary="Actualizar los datos de un usuario",
    responses={
        200: {"description": "Usuario actualizado exitosamente."},
        400: {"description": "Datos no válidos para actualizar el usuario."},
        404: {"description": "Usuario no encontrado."},
        500: {"description": "Error al actualizar el usuario."},
    },
)
async def update_user_router(
    id_usuario: int,
    tipo: str = None,
    nombre: str = None,
    email: str = None,
    password: str = None,
    id_equipo: int = None,
):
    """
    ---
    Endpoint para actualizar los datos de un usuario en la base de datos de manera asincrónica.

    # Flujo del método:\n
    1. `update_user_router(id_usuario, tipo, nombre, email, password, id_equipo)` -> Llama al servicio que actualiza el usuario según los parámetros proporcionados.\n
    2. `update_user_service(id_usuario, tipo, nombre, email, password, id_equipo)` -> Procesa la solicitud y se comunica con los métodos de la base de datos para realizar la actualización.\n
    3. **UserMethods.**`update_user(id_usuario, tipo, nombre, email, password, id_equipo)` -> Ejecuta la consulta de actualización en la base de datos.\n
    ---
    ### Parámetros:\n
    - **id_usuario** (int): ID del usuario a actualizar.\n
    - **tipo** (str, optional): Nuevo tipo del usuario.\n
    - **nombre** (str, optional): Nuevo nombre del usuario.\n
    - **email** (str, optional): Nuevo correo electrónico del usuario.\n
    - **password** (str, optional): Nueva contraseña del usuario.\n
    - **id_equipo** (int, optional): Nuevo ID de equipo del usuario.\n
    ---
    ### Returns:\n
    Resultado de la operación, indicando si la actualización del usuario fue exitosa o si hubo algún error.
    """
    return await update_user_service(id_usuario, tipo, nombre, email, password, id_equipo)

