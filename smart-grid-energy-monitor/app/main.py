import app.models

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.db.database import create_tables
from app.routers.sensor import router as sensor_router
from app.routers.reading import router as reading_router
from app.routers.dashboard import router as dashboard_router

app = FastAPI(
    title="Smart Grid Energy Monitoring System",
    version="1.0.0"
)

# Create database tables
create_tables()

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Configure Jinja2 templates
import os

print("Current Working Directory:", os.getcwd())
print("Templates Path Exists:", os.path.exists("app/templates"))


from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


# Include API routers
app.include_router(sensor_router)
app.include_router(reading_router)
app.include_router(dashboard_router)

# Home Route
@app.get("/")
def root():
    return {
        "message": "Smart Grid Energy Monitoring System API is running."
    }

# Dashboard Route
@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request}
    )