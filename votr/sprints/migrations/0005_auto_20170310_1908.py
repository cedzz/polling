# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-10 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprints', '0004_auto_20170310_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='project_name',
            field=models.CharField(default=None, max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='sprints',
            name='sprint_name',
            field=models.CharField(default=None, max_length=50, unique=True),
        ),
    ]