# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-12 16:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0005_booth_booth_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votes',
            name='candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate', to='teams.Members'),
        ),
        migrations.AlterField(
            model_name='votes',
            name='voter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voter', to='teams.Members'),
        ),
    ]
