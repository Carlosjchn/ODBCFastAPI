from fastapi import FastAPI, HTTPException
from .routes.UsersRouters import router as Prueba_router


app = FastAPI(
    title="API Horarios",
    description="---\n"
    "Esta **API** almacena los datos de los horarios de cada usuarios que"+
    "pertenecen a equipos de trabajo, guardando los horarios personales de cada usuario.\n"+
    "\n" +
    "---",
    version="0.1.0",
)


# Async function to call the synchronous query function
app.include_router(Prueba_router, prefix="/Users", tags=["ENDPOINTS USUARIOS"])

