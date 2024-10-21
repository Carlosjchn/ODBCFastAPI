from fastapi import FastAPI
import pydantic
import jaydebeapi
import mariadb
from sqlalchemy import create_engine, text
import asyncio
from fastapi import FastAPI, HTTPException, Depends
from fastapi.concurrency import run_in_threadpool


# Your database configuration


# Synchronous function to execute queries



# pip freeze > requirements.txt

##############
#   mariadb  #
##############

config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "12345",
    "database": "Peliculas_JDBC",
}



def execute_query_sync(query):
    try:
        conn = mariadb.connect(**config)
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results
    except mariadb.Error as e:
        print(f"Error: {e}")
        return None

# Async function to call the synchronous query function

async def execute_query(query: str):
    return await run_in_threadpool(execute_query_sync, query)

# def execute_query_sync(query):
#     try:
#         conn = mariadb.connect(**config)
#         cursor = conn.cursor()
#         cursor.execute(query)
#         results = cursor.fetchall()
#         conn.close()
#         return results
#     except mariadb.Error as e:
#         print(f"Error: {e}")
#         return None


##############
# jaydebeapi #
##############

conn = jaydebeapi.connect(
    "org.mariadb.jdbc.Driver",
    "jdbc:mariadb://localhost:3306/Peliculas_JDBC",
    ["root", "12345"],
    "C:/DEV/PROYECTOS/PYTHON/JDBCFastAPI/lib/mariadb-java-client-3.4.1.jar",
)

curs = conn.cursor()
curs.execute("SELECT * FROM Peliculas")
result = curs.fetchall()
print(result)
print(type(result))


##############
# SQLalchemy #
##############

# engine = create_engine("mariadb+mariadbconnector://<user>:<password>@<host>[:<port>]/<dbname>")
engine = create_engine("mariadb+mariadbconnector://root:12345@localhost:3306/Peliculas_JDBC")

connection = engine.connect()
print("sqlalchemyyy")
result_sqlal = connection.execute(text("SELECT * FROM Peliculas")).fetchall()
print(result_sqlal)
print(type(result_sqlal))


#######
# API #    
#######

app = FastAPI(
    title="My Awesome API",
    description="This is an awesome API built with FastAPI.",
    version="1.0.0",
    terms_of_service="https://example.com/terms/",
    contact={
        "name": "Support Team",
        "url": "https://example.com/contact",
        "email": "support@example.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)

@app.get("/prueba")
async def read_root():
    return execute_query_sync("SELECT * FROM Peliculas")
    return result
    return str(result_sqlal)


@app.get("/items/")
async def get_items():
    query = "SELECT * FROM Peliculas"
    results = await execute_query(query)
    if results is None:
        raise HTTPException(status_code=500, detail="Database query failed")
    return {"items": results}

