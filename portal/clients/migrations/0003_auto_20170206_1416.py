# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 14:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20170206_1352'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hosting',
            options={'verbose_name_plural': 'Hosting'},
        ),
    ]