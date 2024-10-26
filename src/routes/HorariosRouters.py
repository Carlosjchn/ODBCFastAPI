from fastapi import APIRouter
from ..services.HorariosServices import get_all_horarios_services

router2 = APIRouter()

@router2.get(path = "/all", summary=" ")
async def get_all_horarios_router():
    return await get_all_horarios_services()