from sqlalchemy.orm import Session
from app.models import Sensor
from app.schemas import SensorCreate

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