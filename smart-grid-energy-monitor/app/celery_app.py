from celery import Celery
from celery.schedules import crontab

celery = Celery(
    "smartgrid",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

celery.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="Asia/Kolkata",
    enable_utc=False,

    beat_schedule={
        "aggregate-load-every-5-minutes": {
            "task": "app.tasks.aggregate_load_task",
            "schedule": crontab(minute="*/5"),
        },
    }
)

# Auto-discover Celery tasks
celery.autodiscover_tasks(["app"])