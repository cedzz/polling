# Create your tasks here
from celery.task import periodic_task
from datetime import timedelta

from sprints.models import Sprints
from votr import celeryconfig
from celery import Celery

app = Celery('tasks')
app.config_from_object(celeryconfig)


@periodic_task(run_every=timedelta(hours=3))
def get_sprint_summary():
    Sprints.objects.filter(is_active=1).update(is_active=0)

@periodic_task(run_every=timedelta(hours=3))
def get_active_sprint():
    Sprints.objects.filter(is_active=1).update(is_active=0)