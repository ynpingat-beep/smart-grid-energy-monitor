import json
import asyncio

from app.routers.websocket import broadcast_alert

from app.core.redis import redis_client

from sqlalchemy.orm import Session
from app.models import Sensor, EnergyReading, AggregatedLoad
from app.schemas import SensorCreate

from app.schemas import EnergyReadingCreate

from sqlalchemy import func


def create_sensor(db: Session, sensor: SensorCreate):

    db_sensor = Sensor(**sensor.model_dump())

    db.add(db_sensor)

    db.commit()

    db.refresh(db_sensor)

    return db_sensor

def get_sensors(db: Session):
    return db.query(Sensor).all()



def get_readings(db: Session):
    return db.query(EnergyReading).all()


def create_reading(db: Session, reading: EnergyReadingCreate):

    db_reading = EnergyReading(**reading.model_dump())

    db.add(db_reading)

    db.commit()

    db.refresh(db_reading)

    return db_reading


def get_dashboard_summary(db: Session):

    # Try Redis Cache first
    try:
        cached = redis_client.get("dashboard_summary")

        if cached:
            print("Serving data from Redis Cache")
            return json.loads(cached)

    except Exception as e:
        print("Redis unavailable. Using PostgreSQL.", e)

    # PostgreSQL Queries
    total_sensors = db.query(Sensor).count()

    active_sensors = (
        db.query(Sensor)
        .filter(Sensor.status == "Active")
        .count()
    )

    inactive_sensors = total_sensors - active_sensors

    total_readings = db.query(EnergyReading).count()

    average_voltage = (
        db.query(func.avg(EnergyReading.voltage)).scalar() or 0
    )

    average_current = (
        db.query(func.avg(EnergyReading.current)).scalar() or 0
    )

    average_power = (
        db.query(func.avg(EnergyReading.power)).scalar() or 0
    )

    total_energy = (
        db.query(func.sum(EnergyReading.energy)).scalar() or 0
    )

    summary = {
        "total_sensors": total_sensors,
        "active_sensors": active_sensors,
        "inactive_sensors": inactive_sensors,
        "total_readings": total_readings,
        "average_voltage": round(average_voltage, 2),
        "average_current": round(average_current, 2),
        "average_power": round(average_power, 2),
        "total_energy": round(total_energy, 2),
    }

    # Save to Redis (if available)
    try:
        redis_client.setex(
            "dashboard_summary",
            60,
            json.dumps(summary)
        )
    except Exception:
        print("Could not save to Redis cache.")

    print("Serving data from PostgreSQL")

    return summary


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


def aggregate_load_by_zone(db: Session):

    # Remove old aggregated data
    db.query(AggregatedLoad).delete()

    # Get all sensors
    sensors = db.query(Sensor).all()

    for sensor in sensors:

        readings = (
            db.query(EnergyReading)
            .filter(EnergyReading.sensor_id == sensor.id)
            .all()
        )

        if not readings:
            continue

        avg_voltage = sum(r.voltage for r in readings) / len(readings)
        avg_current = sum(r.current for r in readings) / len(readings)
        total_power = sum(r.power for r in readings)
        total_energy = sum(r.energy for r in readings)

        aggregated = AggregatedLoad(
            zone=sensor.location,
            average_voltage=round(avg_voltage, 2),
            average_current=round(avg_current, 2),
            total_power=round(total_power, 2),
            total_energy=round(total_energy, 2)
        )

        db.add(aggregated)

    db.commit()

    return {
        "message": "Aggregation completed successfully."
    }