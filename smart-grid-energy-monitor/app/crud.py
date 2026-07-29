from sqlalchemy.orm import Session
from app.models import Sensor
from app.schemas import SensorCreate

from app.models import EnergyReading
from app.schemas import EnergyReadingCreate

from sqlalchemy import func


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


def get_dashboard_summary(db: Session):

    total_sensors = db.query(Sensor).count()

    active_sensors = db.query(Sensor).filter(
        Sensor.status == "Active"
    ).count()

    inactive_sensors = total_sensors - active_sensors

    total_readings = db.query(EnergyReading).count()

    average_voltage = db.query(
        func.avg(EnergyReading.voltage)
    ).scalar() or 0

    average_current = db.query(
        func.avg(EnergyReading.current)
    ).scalar() or 0

    average_power = db.query(
        func.avg(EnergyReading.power)
    ).scalar() or 0

    total_energy = db.query(
        func.sum(EnergyReading.energy)
    ).scalar() or 0

    return {
        "total_sensors": total_sensors,
        "active_sensors": active_sensors,
        "inactive_sensors": inactive_sensors,
        "total_readings": total_readings,
        "average_voltage": round(average_voltage, 2),
        "average_current": round(average_current, 2),
        "average_power": round(average_power, 2),
        "total_energy": round(total_energy, 2)
    }


def get_recent_sensors(db: Session):
    return db.query(Sensor).order_by(Sensor.id.desc()).limit(5).all()


def get_chart_data(db: Session):
    readings = (
        db.query(EnergyReading)
        .order_by(EnergyReading.id.desc())
        .limit(10)
        .all()
    )

    readings.reverse()

    return [
        {
            "id": reading.id,
            "voltage": reading.voltage,
            "power": reading.power
        }
        for reading in readings
    ]