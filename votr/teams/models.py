from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.dispatch import receiver
from django.db.models.signals import post_save


class Teams(models.Model):

    company = models.CharField(max_length=50)
    team_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    image = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.team_name


class Members(models.Model):

    team = models.ForeignKey(Teams, null=True, blank=False)
    user = models.OneToOneField(User, null=True, blank=False, editable=False)
    email = models.EmailField(null=True, blank=False)
    name = models.CharField(max_length=50, editable=False)
    age = models.IntegerField(null=True, blank=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Members.objects.create(user=instance, name=instance.username)

    def __unicode__(self):
        return self.name