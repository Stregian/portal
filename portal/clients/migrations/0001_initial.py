# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 12:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Hosting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=7)),
                ('renewal_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('url', models.URLField()),
                ('dob', models.DateTimeField()),
                ('fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Client', verbose_name='Client')),
            ],
        ),
        migrations.AddField(
            model_name='hosting',
            name='fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Website'),
        ),
        migrations.AddField(
            model_name='hosting',
            name='fk_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Client'),
        ),
    ]