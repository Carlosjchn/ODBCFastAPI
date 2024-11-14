from fastapi import FastAPI, HTTPException
from .routes.UsersRouters import router as router_usuario
from .routes.HorariosRouters import router2 as router_horarios
from .routes.EquiposRouter import router as router_equipos
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="API Horarios",
    description="---\n"
    "Esta **API** almacena los datos de los horarios de cada usuarios que"
    + "pertenecen a equipos de trabajo, guardando los horarios personales de cada usuario.\n"
    + "\n"
    + "---",
    version="0.1.0",
)



app.include_router(
    router_usuario,
    prefix="/User",
    tags=["USERS ENDPOINTS"],
)

app.include_router(
    router_horarios,
    prefix="/Horario",
    tags=["HORARIOS ENDPOINTS"],
)

app.include_router(
    router_equipos,
    prefix="/Equipo",
    tags=["EQUIPOS ENDPOINTS"],
)
