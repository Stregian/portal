# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-14 17:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0007_auto_20170214_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 14, 17, 31, 21, 4171, tzinfo=utc)),
        ),
    ]