from fastapi import APIRouter
from ..services.EquipoService import get_all_equipos_service
from ..models.EquipoModel import Equipo_Default_Response

router = APIRouter()

@router.get("/all")
async def get_all_equipos_router():
    return await get_all_equipos_service()
