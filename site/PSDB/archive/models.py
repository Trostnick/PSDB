from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from PIL import Image
import shedule.models


class Planet(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField()
    image = models.ImageField(upload_to='static/images/Planet/', blank=True)

    def __unicode__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)
    is_st_nab = models.BooleanField()
    birth_date = models.CharField(max_length=100, blank=True, null=True)
    were_burn = models.CharField(max_length=100, blank=True, null=True)
    planet = models.ForeignKey(Planet, null=True, on_delete=models.SET_NULL, blank=True)
    father = models.CharField(max_length=100)
    mother = models.CharField(max_length=100)
    education = models.TextField()
    work_before = models.TextField()
    coming_date = models.CharField(max_length=100, blank=True, null=True)
    career = models.TextField()
    image = models.ImageField(upload_to='static/images/Person/', blank=True)

    def __unicode__(self):
        return self.name


class BG(models.Model):
    name = models.CharField(max_length=200)
    info = models.TextField()
    st_nab = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='static/images/BG/', blank=True)
    is_active = models.BooleanField(default=True)
    last_st_nab = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL, blank=True)

    def __unicode__(self):
        return self.name


class Mission(models.Model):
    name = models.CharField(max_length=50)
    watch = models.IntegerField()
    target = models.TextField()
    info = models.TextField()
    result = models.CharField(max_length=50)
    planet_text = models.TextField(blank=True)
    planet = models.ForeignKey(Planet, null=True, on_delete=models.SET_NULL, blank=True)
    bg = models.ForeignKey(BG, null=True, on_delete=models.SET_NULL, blank=True)

    def __unicode__(self):
        return self.name


class Point(models.Model):
    value = models.IntegerField()
    watcher = models.ForeignKey(shedule.models.Watcher, on_delete=models.CASCADE)
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)

    def __unicode__(self):
        name = self.watcher.name + ' ' + self.mission.name
        return name
    


