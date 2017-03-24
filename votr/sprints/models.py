from __future__ import unicode_literals

from django.db import models

# Create your models here.
from teams.models import Teams


class Projects(models.Model):

    team = models.ForeignKey(Teams)
    project_name = models.CharField(max_length=50, default=None, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField(default=None)
    end_date = models.DateTimeField(default=None, null=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.project_name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class Sprints(models.Model):

    project = models.ForeignKey(Projects)
    sprint_name = models.CharField(max_length=50, default=None, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField(default=None)
    end_date = models.DateTimeField(default=None, null=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.sprint_name

    class Meta:
        verbose_name = 'Sprint'
        verbose_name_plural = 'Sprints'