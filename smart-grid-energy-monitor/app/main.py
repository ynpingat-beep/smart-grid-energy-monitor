import app.models

from fastapi import FastAPI
from app.db.database import create_tables
from app.routers.sensor import router as sensor_router
from app.routers.dashboard import router as dashboard_router
from app.routers.reading import router as reading_router

app = FastAPI(
    title="Smart Grid Energy Monitoring System",
    version="1.0.0"
)

create_tables()

app.include_router(sensor_router)
app.include_router(reading_router)
app.include_router(dashboard_router)

@app.get("/")
def root():
    return {
        "message": "Smart Grid Energy Monitoring System API is running."
    }