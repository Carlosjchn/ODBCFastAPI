from fastapi.concurrency import run_in_threadpool
import mariadb
from .Config_bbdd import config as config_bbdd


def execute_query_sync(query):
    try:
        conn = mariadb.connect(**config_bbdd)
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results
    except mariadb.Error as e:
        print(f"Error: {e}")
        return None


async def execute_query(query: str):
    return await run_in_threadpool(execute_query_sync, query)