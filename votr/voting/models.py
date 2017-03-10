from __future__ import unicode_literals

from django.db import models

# Create your models here.
from sprints.models import Sprints
from teams.models import Members


class Booth(models.Model):

    sprint = models.ForeignKey(Sprints)
    created_at = models.DateTimeField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=False)


class Votes(models.Model):

    PARAMETER_CHOICES = (
        (1, "Idea"),
        (2, "Enthu"),
        (3, "Quality"),
        (4, "Quantum"),
    )

    booth = models.ForeignKey(Booth)
    candidate = models.ForeignKey(Members)
    voter = models.CharField(max_length=50, default=None)
    parameter = models.IntegerField(choices=PARAMETER_CHOICES, default=None)
    comments = models.TextField(max_length=200)
    created_at = models.DateTimeField()