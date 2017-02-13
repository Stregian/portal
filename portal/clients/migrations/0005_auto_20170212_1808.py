# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-12 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_auto_20170206_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='contact',
            field=models.CharField(max_length=20, verbose_name='Contact number'),
        ),
        migrations.AlterField(
            model_name='website',
            name='dob',
            field=models.DateField(verbose_name='Date of birth'),
        ),
    ]