from app.celery_app import celery

from app.db.database import SessionLocal

from app.crud import aggregate_load_by_zone


@celery.task
def aggregate_load_task():

    db = SessionLocal()

    try:
        result = aggregate_load_by_zone(db)
        print(result)

    finally:
        db.close()