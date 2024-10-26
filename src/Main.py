from fastapi import FastAPI, HTTPException
from .routes.UsersRouters import router as router_usuario
from .routes.HorariosRouters import router2 as router_horarios


app = FastAPI(
    title="Gestor Horarios",
    description="Esta API almacena los datos de los horarios de cada usuarios que"+
                "pertenecen a equipos de trabajo, guardando los horarios personales de cada usuario.",
    version="1.0.0",
    
)


# Async function to call the synchronous query function
app.include_router(router_usuario, 
                   prefix="/Users",
                   tags=["USERS ENDPOINTS"],
                   )
app.include_router(router_horarios, 
                   prefix="/Horarios",
                   tags=["HORARIOS ENDPOINTS"],
                   )


