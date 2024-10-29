from fastapi import APIRouter
from ..services.UsersServices import get_all_users_service, get_user_byId_service, get_all_UserDetails_service, get_Details_byID_service, get_all_info_details_service
from ..models.UserModel import User, UserDetails, UserBasicDetails


router = APIRouter()


@router.get("/all",
    summary="Get_all_users",
    responses={
        200: {
            "description": "Successful operation.",
            "content": {
                "application/json": {
                    "example": {
                        "id_usuario": "int",
                        "tipo": "tipo",
                        "nombre": "nombre_usuario",
                        "email": "correo_usuario@gmail.com",
                        "password": "contraseña123",
                        "id_equipo": "int",
                    }
                }
            },
        },
        500: {
            "description": "Error executing query."
        }
    },
    response_model=list[User]
)
async def get_all_users_router(): 
    """
    ---
    Método para consultar todos los usuarios en la base de datos de manera asincrona.
    
    # Flujo del método:\n
    1. `get_all_users_router()` -> Llama al servicio encargado de obtener los usuarios.\n
    2. `get_all_users_service()` -> Procesa la solicitud y se comunica con los métodos de la base de datos.\n
    3. **UserMethods**.`fetch_all_users()` -> Ejecuta la consulta en la base de datos y retorna los usuarios.\n
    ---
    ### Returns:\n    
    Lista de todos los usuarios disponibles en la base de datos.
    
    """ 
    return await get_all_users_service()

@router.get(
    "/byId/{id}",
    summary="Get user by ID",
    responses={
        200: {
            "description": "Successful operation.",
            "content": {
                "application/json": {
                    "example": {
                        "id_usuario": "int",
                        "tipo": "tipo",
                        "nombre": "nombre_usuario",
                        "email": "correo_usuario@gmail.com",
                        "password": "contraseña123",
                        "id_equipo": "int",
                    }
                }
            },
        },
        404: {
            "description": "User not found."
        },
        500: {
            "description": "Error executing query."
        }
    },
    response_model=User
)
async def get_user_byId_router(id: int):
    """
    ---
    Método para consultar un usuario en la base de datos por su ID de manera asincrona.
    
    # Flujo del método:\n
    1. `get_user_byId_router(id)` -> Llama al servicio encargado de obtener el usuario con el ID especificado.\n
    2. `get_user_byId_service(id)` -> Procesa la solicitud y se comunica con los métodos de la base de datos.\n
    3. **UserMethods**.`fetch_user_by_id(id)` -> Ejecuta la consulta en la base de datos y retorna el usuario.\n
    ---
    ### Parameters:\n
    - ***ID*** (int): ID del usuario que se desea consultar.
    ---
    ### Returns:\n    
    Información del usuario correspondiente al ID proporcionado, si existe.
    """
    return await get_user_byId_service(id)

@router.get("/allDetails",
    summary="Get all user details",
    responses={
        200: {
            "description": "Successful operation.",
            "content": {
                "application/json": {
                    "example": {
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
                                "hora_fin": "HH:MM:SS"
                            }
                        ]
                    }
                }
            },
        },
        500: {
            "description": "Error executing query."
        }
    },
    response_model=list[UserBasicDetails]
)
async def get_all_UserDetails_router():
    """
    ---
    Método para consultar todos los detalles de los usuarios en la base de datos de manera asincrónica.
    
    # Flujo del método:\n
    1. `get_all_UserDetails_router()` -> Llama al servicio que obtiene detalles completos de los usuarios.\n
    2. `get_all_UserDetails_service()` -> Procesa la solicitud y se comunica con los métodos de la base de datos.\n
    3. **UserMethods**.`fetch_all_user_details()` -> Ejecuta la consulta en la base de datos y retorna la información detallada de los usuarios.\n
    ---
    ### Returns:\n    
    Lista de todos los usuarios con sus detalles completos, incluyendo horarios, si están disponibles.
    """
    return await get_all_UserDetails_service()


@router.get("/DetailsById/{id}",
    summary="Get user details by ID",
    responses={
        200: {
            "description": "Successful operation.",
            "content": {
                "application/json": {
                    "example": [{
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
                                "hora_fin": "HH:MM:SS"
                            },
                        ]
                    }]
                }
            },
        },
        404: {
            "description": "User details not found."
        },
        500: {
            "description": "Error executing query."
        }
    },
    response_model= list[UserBasicDetails]
)
async def get_Details_ById_router(id: int):
    """
    ---
    Método para consultar los detalles de un usuario en la base de datos por su ID de manera asincrónica.
    
    # Flujo del método:\n
    1. `get_Details_ById_router(id)` -> Llama al servicio que obtiene los detalles del usuario con el ID especificado.\n
    2. `get_Details_byID_service(id)` -> Procesa la solicitud y se comunica con los métodos de la base de datos.\n
    3. **UserMethods**.`fetch_user_details_by_id(id)` -> Ejecuta la consulta en la base de datos y retorna los detalles del usuario.\n
    ---
    ### Parameters:\n
    - ***ID*** (int): ID del usuario cuyos detalles se desean consultar.
    ---
    ### Returns:\n    
    Información detallada del usuario correspondiente al ID proporcionado, incluyendo horarios, si están disponibles.
    """
    return await get_Details_byID_service(id)


@router.get(
    "/allInfoGlobal",
    summary="Get all global information for users",
    responses={
        200: {
            "description": "Successful operation.",
            "content": {
                "application/json": {
                    "example": {
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
                                "horas_fin_act": "HH:MM:SS"
                            }
                        ],
                        "horarios": [
                            {
                                "id_horario": "int",
                                "fecha": "YYYY-MM-DD",
                                "hora_inicio": "HH:MM:SS",
                                "hora_fin": "HH:MM:SS"
                            }
                        ]
                    }
                }
            },
        },
        500: {
            "description": "Error executing query."
        }
    },
    response_model=list[UserDetails]
)
async def get_all_info_details_router():
    """
    ---
    Método para consultar la información global completa de los usuarios en la base de datos de manera asincrónica.
    
    # Flujo del método:\n
    1. `get_all_info_details_router()` -> Llama al servicio que obtiene toda la información relacionada con los usuarios, incluyendo detalles de equipo y horarios.\n
    2. `get_all_info_details_service()` -> Procesa la solicitud y se comunica con los métodos de la base de datos.\n
    3. **UserMethods**.`fetch_all_info_details()` -> Ejecuta la consulta en la base de datos y retorna los detalles completos de cada usuario, incluyendo la información de equipo y horarios.\n
    --- 
    ### Returns:\n    
    Lista de todos los usuarios con su información completa, que incluye:
    - Información básica de usuario.
    - Detalles de equipo asociados, si existen.
    - Información de horarios asignados, si están disponibles.
    """
    return await get_all_info_details_service()
