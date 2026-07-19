from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from sqlalchemy import ForeignKey, Float
from sqlalchemy.orm import relationship

from app.db.database import Base


class Sensor(Base):
    from sqlalchemy.orm import relationship
    readings = relationship("EnergyReading", back_populates="sensor")

    __tablename__ = "sensors"

    id = Column(Integer, primary_key=True, index=True)
    sensor_name = Column(String(100), nullable=False)
    location = Column(String(100), nullable=False)
    status = Column(String(20), default="Active")
    created_at = Column(DateTime, default=datetime.utcnow)



class EnergyReading(Base):
    __tablename__ = "energy_readings"

    id = Column(Integer, primary_key=True, index=True)

    sensor_id = Column(Integer, ForeignKey("sensors.id"))

    voltage = Column(Float, nullable=False)

    current = Column(Float, nullable=False)

    power = Column(Float, nullable=False)

    energy = Column(Float, nullable=False)

    timestamp = Column(DateTime, default=datetime.utcnow)
    
    sensor = relationship("Sensor", back_populates="readings")