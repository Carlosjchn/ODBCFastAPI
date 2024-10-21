from dotenv import load_dotenv
import os

load_dotenv()

config = {
        "host": os.getenv("DATABASE_HOST"),
        "port": int(os.getenv("DATABASE_PORT")),
        "user": os.getenv("DATABASE_USER"),
        "password": os.getenv("DATABASE_PASSWORD"),
        "database": os.getenv("DATABASE_NAME")
    }

print(os.getcwd())
