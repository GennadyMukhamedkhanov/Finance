import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

app = Celery('conf')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = 'redis://redis:6379/0'
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'sending_letter': {
        'task': 'api.tasks.sending_letter_once_hour',
        'schedule': 5.0,
    }
}
