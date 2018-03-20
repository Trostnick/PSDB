# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-20 05:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shedule', '0003_auto_20170329_0304'),
        ('archive', '0015_auto_20180319_1929'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('info', models.TextField()),
                ('clas', models.IntegerField()),
                ('date', models.DateField()),
                ('nabs', models.ManyToManyField(blank=True, related_name='challenges', to='shedule.Watcher')),
            ],
        ),
    ]
