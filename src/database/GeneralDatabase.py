from fastapi.concurrency import run_in_threadpool
import mariadb
from .ConfigDatabase import config
from fastapi import HTTPException

#############################
# Metodos básicos para BBDD #
#############################


class GeneralMethods:
    ##############
    # Conexiones #
    ##############
    @staticmethod
    def connection():
        try:
            conn = mariadb.connect(**config)
            return conn
        except mariadb.Error as e:
            raise HTTPException(
                status_code=500, detail=f"Error connecting to MariaDB Platform: {e}"
            )

    @staticmethod
    def disconnect(conn):
        if conn:
            conn.close()

    ##################
    # fetch de datos #
    ##################
        """
        EJEMPLO QUERY USO
        query = "SELECT *.u FROM users u"
        """
    def execute_query(query):
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
            raise HTTPException(
                status_code=500, detail=f"Error executing query as async: {e}"
            )
            
            
    ##################
    # insertar datos #        
    ##################
    """
    EJEMPLO QUERY USO
    query = "INSERT INTO users (name, email, age) VALUES (:name, :email, :age)"
    params = {"name": "John Doe", "email": "john.doe@example.com", "age": 30}
    """
    @staticmethod
    def insert_data(query: str, params: dict):
        try:
            conn = GeneralMethods.connection()
            cur = conn.cursor()
            cur.execute(query, params)
            conn.commit()  # Commit the transaction
            return {"message": "Data inserted successfully"}
        except mariadb.Error as e:
            raise HTTPException(status_code=500, detail=f"Error inserting data: {e}")
        finally:
            GeneralMethods.disconnect(conn)

    @staticmethod
    async def insert_data_async(query: str, params: dict):
        try:
            return await run_in_threadpool(GeneralMethods.insert_data, query, params)
        except HTTPException as e:
            raise e

    ################
    # update datos #
    ################
    """
    EJEMPLO QUERY USO
    query = "UPDATE users SET email = :email, age = :age WHERE name = :name"
    params = {"email": "new.email@example.com", "age": 35, "name": "John Doe"}
    """
    @staticmethod
    def update_data(query: str):
        try:
            conn = GeneralMethods.connection()
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()  # Commit the transaction to apply the update
            return {"message": "Data updated successfully"}
        except mariadb.Error as e:
            raise HTTPException(status_code=500, detail=f"Error updating data: {e}")
        finally:
            GeneralMethods.disconnect(conn)

    @staticmethod
    async def update_data_async(query: str):
        try:
            return await run_in_threadpool(GeneralMethods.update_data, query)
        except HTTPException as e:
            raise e

    ##################
    # eliminar datos #
    ##################
    
    """
    EJEMPLO QUERY USO
    query = "DELETE FROM users WHERE name = :name"
    params = {"name": "John Doe"}
    """

    @staticmethod
    def delete_data(query: str):
        try:
            conn = GeneralMethods.connection()
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()  # Commit the transaction to confirm deletion
            return {"message": "Data deleted successfully"}
        except mariadb.Error as e:
            raise HTTPException(status_code=500, detail=f"Error deleting data: {e}")
        finally:
            GeneralMethods.disconnect(conn)

    @staticmethod
    async def delete_data_async(query: str):
        try:
            return await run_in_threadpool(GeneralMethods.delete_data, query)
        except HTTPException as e:
            raise e
