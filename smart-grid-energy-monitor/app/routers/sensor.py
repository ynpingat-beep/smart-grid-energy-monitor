from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.schemas import SensorCreate
from app.crud import create_sensor, get_sensors

router = APIRouter(prefix="/sensors", tags=["Sensors"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def add_sensor(sensor: SensorCreate, db: Session = Depends(get_db)):
    return create_sensor(db, sensor)

@router.get("/")
def read_sensors(db: Session = Depends(get_db)):
    return get_sensors(db)