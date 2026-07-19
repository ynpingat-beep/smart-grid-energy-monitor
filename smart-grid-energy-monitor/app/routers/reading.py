from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.schemas import EnergyReadingCreate
from app.crud import create_reading, get_readings

router = APIRouter(prefix="/readings", tags=["Energy Readings"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def add_reading(reading: EnergyReadingCreate, db: Session = Depends(get_db)):
    return create_reading(db, reading)


@router.get("/")
def read_readings(db: Session = Depends(get_db)):
    return get_readings(db)