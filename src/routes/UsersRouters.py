from fastapi import APIRouter, HTTPException
from ..services.UsersServices import get_all_users_service
from ..models.UserModel import User


router = APIRouter()



@router.get("/all",
    summary="Get_all_users",
    responses={
        200: {
            "description": "Successful operation.",
            "content": {
                "application/json": {
                    "example": {
                        "id_usuario": 1,
                        "tipo": "tipo",
                        "nombre": "nombre_usuario",
                        "email": "correo_usuario@gmail.com",
                        "password": "contraseña123",
                        "id_equipo": 1,
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






