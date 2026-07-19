from sqlalchemy.orm import Session
from app.models import Sensor
from app.schemas import SensorCreate

from app.models import EnergyReading
from app.schemas import EnergyReadingCreate



def create_sensor(db: Session, sensor: SensorCreate):
    db_sensor = Sensor(
        sensor_name=sensor.sensor_name,
        location=sensor.location,
        status=sensor.status
    )
    db.add(db_sensor)
    db.commit()
    db.refresh(db_sensor)
    return db_sensor

def get_sensors(db: Session):
    return db.query(Sensor).all()



def create_reading(db: Session, reading: EnergyReadingCreate):
    db_reading = EnergyReading(**reading.model_dump())
    db.add(db_reading)
    db.commit()
    db.refresh(db_reading)
    return db_reading


def get_readings(db: Session):
    return db.query(EnergyReading).all()