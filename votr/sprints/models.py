from __future__ import unicode_literals

from django.db import models

# Create your models here.
from teams.models import Teams


class Projects(models.Model):
    team = models.ForeignKey(Teams)
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(default=None)
    end_date = models.DateTimeField(default=None)
    is_active = models.BooleanField(default=False)


class Sprints(models.Model):

    company = models.CharField(max_length=50)
    team = models.ForeignKey(Teams)
    project = models.ForeignKey(Projects)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField(default=None)
    end_date = models.DateTimeField(default=None)
    is_active = models.BooleanField(default=True)