from __future__ import unicode_literals

from django.db import models

# Create your models here.
from teams.models import Teams, Members


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

    @classmethod
    def get_active_sprint(cls):
        try:
            return cls.objects.get(is_active=1)
        except cls.DoesNotExist:
            return None

    class Meta:
        verbose_name = 'Sprint'
        verbose_name_plural = 'Sprints'


class SprintSummary(models.Model):

    sprint = models.ForeignKey(Sprints)
    member = models.ForeignKey(Members)
    ticket = models.CharField(max_length=50, default=None)
    ticket_desc = models.CharField(max_length=100, default=None)
    points = models.IntegerField(default=0)
    due_date = models.DateField()
    status = models.CharField(max_length=50, default=None)
    comments = models.CharField(max_length=200, default=None)

    def __unicode__(self):
        return self.ticket

    class Meta:
        verbose_name = 'Sprint Summary'
        verbose_name_plural = 'Sprint Summary'