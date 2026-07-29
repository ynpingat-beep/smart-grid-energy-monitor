from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.crud import get_dashboard_summary, get_recent_sensors

from app.crud import (
    get_dashboard_summary,
    get_recent_sensors,
    get_chart_data
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/summary")
def dashboard_summary(db: Session = Depends(get_db)):
    return get_dashboard_summary(db)

@router.get("/recent")
def recent_sensors(db: Session = Depends(get_db)):
    return get_recent_sensors(db)

@router.get("/chart")
def chart_data(db: Session = Depends(get_db)):
    return get_chart_data(db)