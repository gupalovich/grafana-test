import random
import time

from django.contrib.auth import get_user_model

from config import celery_app

User = get_user_model()


@celery_app.task(bind=True, queue="low_priority")
def trigger_long_task(self):
    queue_name = self.request.delivery_info["routing_key"]

    time.sleep(random.randint(5, 10))

    return queue_name


@celery_app.task(bind=True, queue="high_priority")
def trigger_short_task(self):
    queue_name = self.request.delivery_info["routing_key"]

    time.sleep(2)

    return queue_name


@celery_app.task(bind=True)
def trigger_long_fail_task(self):
    time.sleep(random.randint(5, 10))
    raise ValueError("Test")
