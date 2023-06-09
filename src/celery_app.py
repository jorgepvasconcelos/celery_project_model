from celery import Celery

import celeryconfig
from src.settings import REDIS_URL, CELERY_APP_NAME

app = Celery(
    main=CELERY_APP_NAME,
    backend=REDIS_URL,
    broker=REDIS_URL,
    include=['src.tasks'],
    config_source=celeryconfig
)

if __name__ == '__main__':
    app.start()
