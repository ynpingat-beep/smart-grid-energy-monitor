from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.schemas import EnergyReadingCreate
from app.crud import create_reading, get_readings

from app.routers.websocket import broadcast_alert
import asyncio

router = APIRouter(prefix="/readings", tags=["Energy Readings"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def add_reading(reading: EnergyReadingCreate, db: Session = Depends(get_db)):

    new_reading = create_reading(db, reading)

    try:

        loop = asyncio.get_event_loop()

        if new_reading.voltage > 235:
            loop.create_task(
                broadcast_alert(
                    f"🚨 High Voltage Alert ({new_reading.voltage} V)"
                )
            )

        if new_reading.power > 1250:
            loop.create_task(
                broadcast_alert(
                    f"⚡ High Power Alert ({new_reading.power} W)"
                )
            )

    except Exception as e:
        print("Alert Error:", e)

        return new_reading


@router.get("/")
def read_readings(db: Session = Depends(get_db)):
    return get_readings(db)