from datetime import timedelta

CELERY_BROKER_URL = 'redis://sixads_redis:6379'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

CELERY_BEAT_SCHEDULE = {
    'scrap_channel': {
        'task': 'app.tasks.scrap_channel',
        'schedule': timedelta(hours=2),
    }
}
