from pydantic import BaseModel

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