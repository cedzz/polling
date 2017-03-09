from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Teams(models.Model):

    company = models.CharField(max_length=50)
    team_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_created=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)


class Members(models.Model):

    team = models.ForeignKey(Teams)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    is_active = models.BooleanField(default=False)
    voter_id = models.IntegerField(auto_created=True)
    created_at = models.DateTimeField(auto_created=True)
    modified_at = models.DateTimeField(auto_now_add=True)