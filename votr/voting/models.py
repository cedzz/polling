from __future__ import unicode_literals

from django.db import models

# Create your models here.

from sprints.models import Sprints
from teams.models import Members


class VotingParams(models.Model):

    parameter_name = models.CharField(max_length=50, default=None)
    comments = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.parameter_name

class Booth(models.Model):

    sprint = models.ForeignKey(Sprints)
    booth_name = models.CharField(max_length=50, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(default=None)
    end_date = models.DateTimeField(default=None, null=True)
    is_active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.booth_name

class Votes(models.Model):

    booth = models.ForeignKey(Booth)
    candidate = models.ForeignKey(Members, related_name='candidate')
    voter = models.ForeignKey(Members, related_name='voter')
    parameter = models.ForeignKey(VotingParams)
    comments = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)