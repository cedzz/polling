# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-22 18:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprints', '0015_sprintsummary_reporter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sprintsummary',
            old_name='member',
            new_name='assignee',
        ),
    ]
