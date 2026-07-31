from app.celery_app import celery
from datetime import datetime

@celery.task
def dashboard_background_task():
    print("Background task executed at:", datetime.now())
    return "Task Completed Successfully"