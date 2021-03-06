# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-10 14:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0002_auto_20170310_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='votes',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2017, 3, 10, 14, 5, 28, 607568, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booth',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='booth',
            name='end_date',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='booth',
            name='start_date',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='votes',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
