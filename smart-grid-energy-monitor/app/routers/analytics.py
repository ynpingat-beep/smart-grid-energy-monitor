from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.models import AggregatedLoad

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/load")
def get_aggregated_load(db: Session = Depends(get_db)):

    data = db.query(AggregatedLoad).all()

    return data