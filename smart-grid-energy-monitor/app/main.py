import app.models

from fastapi import FastAPI
from app.db.database import create_tables

app = FastAPI(
    title="Smart Grid Energy Monitoring System",
    version="1.0.0"
)

create_tables()

@app.get("/")
def root():
    return {
        "message": "Smart Grid Energy Monitoring System API is running."
    }