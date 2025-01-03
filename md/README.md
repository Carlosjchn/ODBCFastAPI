# User API Documentation

# INFORMACIÓN DEL PROYECTO

- **Workframe**: FastAPI
- **Lenguaje**: Python
- **Dependencias**: 
    - **fastapi:** Framework web rápido para construir APIs en Python.
    - **pydantic:** Biblioteca para validación y manejo de datos, esencial en FastAPI para definir modelos de datos.
    - **uvicorn:** Servidor ASGI rápido, utilizado para desplegar aplicaciones FastAPI.
    - **python-dotenv:** Carga variables de entorno desde un archivo .env, útil para configuración de aplicaciones.
    - **mariadb:** Conector de base de datos específico para MariaDB, usado para interactuar con la base de datos MariaDB.
---
## INICIAR EL PROYECTO:

Moverse a la carpeta ***ODBCFastAPI***:

```
cd ODBCFastAPI
```
***Ejemplo ruta correcta:***

**PS D:\Programacion\Python Projects\ODBCFastAPI>**

Una vez en la ruta instalar dependencias del proyecto, usando : 
```
pip install -r md/requirements
```

Para iniciar el proyecto ejecutar: 

```
uvicorn src.Main:app --reload
```
---
## DOCUMENTACION DEL PROYECTO

FastAPI proporciona dos documentaciones accesibles desde las rutas utiles de tu proyecto:

***Swagger*** : URL_API/docs

***Redocs*** : URL_API/redoc

En mi caso seria estas rutas:

***Swagger*** : http://127.0.0.1:8000/docs

***Redoc*** : http://127.0.0.1:8000/redoc

Estas plataformas de documentacion proporcionan informacion sobre los endpoints, posibles respuestas y estructura interna del proyecto. Swagger incluye funcionalidad para probar los endpoints del proyecto, mientras que Redoc da una intefaz mas limpia y facil sobre los endpoints y sus posibles respuestas.
