# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='part_time',
            field=models.IntegerField(default=1),
        ),
    ]