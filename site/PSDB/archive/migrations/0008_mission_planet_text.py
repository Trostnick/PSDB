# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-19 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0007_auto_20170819_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='planet_text',
            field=models.TextField(blank=True),
        ),
    ]