from pydantic import BaseModel
from datetime import datetime

class SensorCreate(BaseModel):
    sensor_name: str
    location: str
    status: str

class SensorResponse(BaseModel):
    id: int
    sensor_name: str
    location: str
    status: str

    class Config:
        from_attributes = True


class EnergyReadingCreate(BaseModel):
    sensor_id: int
    voltage: float
    current: float
    power: float
    energy: float


class EnergyReadingResponse(EnergyReadingCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True