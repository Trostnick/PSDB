# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 20:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('max_students', models.IntegerField(default=12)),
                ('place', models.CharField(max_length=50)),
                ('day', models.IntegerField(default=1)),
                ('previous_lesson_day', models.IntegerField(blank=True, default=0)),
                ('start_time', models.TimeField()),
                ('short_info', models.TextField()),
                ('is_specialization', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-day'],
                'db_table': 'lessons',
            },
        ),
        migrations.CreateModel(
            name='Watcher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('bg', models.CharField(blank=True, max_length=30)),
                ('photo', models.ImageField(blank=True, upload_to='static/images/Watcher/')),
                ('info', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'watchers',
            },
        ),
        migrations.AddField(
            model_name='lesson',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='student_lessons', to='shedule.Watcher'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_lessons', to='shedule.Watcher'),
        ),
    ]
