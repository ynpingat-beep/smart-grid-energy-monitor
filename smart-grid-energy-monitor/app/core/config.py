from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://postgres:yash9477@localhost:5432/smart_grid_db"
)

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "development-secret-key"
)

DEBUG = os.getenv(
    "DEBUG",
    "False"
).lower() == "true"

print("DATABASE_URL:", DATABASE_URL)