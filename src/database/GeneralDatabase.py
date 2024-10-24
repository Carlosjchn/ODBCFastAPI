from fastapi.concurrency import run_in_threadpool
import mariadb
from .ConfigDatabase import config
from fastapi import HTTPException

class GeneralMethods:
    @staticmethod
    def connection():
        try:
            conn = mariadb.connect(**config)
            return conn
        except mariadb.Error as e:
            raise HTTPException(status_code=500, detail=f"Error connecting to MariaDB Platform: {e}")

    @staticmethod
    def disconnect(conn):
        if conn:
            conn.close()

    def execute_query(query):
        conn = None
        try:
            conn = GeneralMethods.connection()  # Call static method without self
            cur = conn.cursor()
            cur.execute(query)
            return cur.fetchall()  # Return the result of the query
        except mariadb.Error as e:
            raise HTTPException(status_code=500, detail=f"Error executing query: {e}")
        finally:
            GeneralMethods.disconnect(conn)  # Call static method without self

    @staticmethod
    async def execute_query_async(query):
        try:
            # Run the static method in a thread pool and await its result
            return await run_in_threadpool(GeneralMethods.execute_query, query)
        except HTTPException as e:
            raise e  # Re-raise the HTTPException for handling at a higher level
        except mariadb.Error as e:
            raise HTTPException(status_code=500, detail=f"Error executing query as async: {e}")