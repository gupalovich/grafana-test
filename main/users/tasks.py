import random
import time
from django.contrib.auth import get_user_model

from config import celery_app

User = get_user_model()


@celery_app.task()
def get_users_count():
    """A pointless Celery task to demonstrate usage."""
    return User.objects.count()


@celery_app.task()
def trigger_long_task():
    time.sleep(random.randint(5, 10))
    
@celery_app.task()
def trigger_long_fail_task():
    time.sleep(random.randint(5, 10))
    raise ValueError("Test")