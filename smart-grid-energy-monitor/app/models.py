from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.db.database import Base


class Sensor(Base):
    __tablename__ = "sensors"

    id = Column(Integer, primary_key=True, index=True)
    sensor_name = Column(String(100), nullable=False)
    location = Column(String(100), nullable=False)
    status = Column(String(20), default="Active")
    created_at = Column(DateTime, default=datetime.utcnow)