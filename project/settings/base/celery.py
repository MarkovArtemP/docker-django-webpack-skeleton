INSTALLED_APPS = INSTALLED_APPS + ('djcelery', 'djkombu', )

BROKER_URL = 'redis://localhost:6379/0'

CELERY_SEND_EVENTS = True

CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'