import os
from celery.schedules import crontab
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'metsenat.settings')

app = Celery('metsenat')

app.conf.broker_url = "redis://localhost:6379/0"
app.conf.timezone = "Asia/Tashkent"
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    # 'send-students-info': {
    #     'task': 'sponsor.tasks.send_students_info',
    #     'schedule': crontab(minute='*/1')
    # },
    # 'send-status-info': {
    #     'task': 'sponsor.tasks.send_status_info',
    #     'schedule': crontab(minute='*/1')
    # }
}
