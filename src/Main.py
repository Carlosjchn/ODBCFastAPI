from fastapi import FastAPI, HTTPException
from .routes.Main_router import router as Prueba_router
from .database.Pruebas_bbdd import execute_query



app = FastAPI(
    title="Gestor Horarios",
    description="Esta API almacena los datos de los horarios de cada usuarios que"+
                "pertenecen a equipos de trabajo, guardando los horarios personales de cada usuario.",
    version="1.0.0",
)

@app.get("/items/" , tags=["Prueba"])
async def get_items():
    query = "SELECT * FROM usuario"
    results = await execute_query(query)
    if results is None:
        raise HTTPException(status_code=500, detail="Database query failed")
    return {"items": results}



# Async function to call the synchronous query function
app.include_router(Prueba_router, prefix="/JDBC")

