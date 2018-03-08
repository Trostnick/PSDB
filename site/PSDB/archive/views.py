# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import BG
from .models import Planet
from .models import Person
from .models import Mission
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, reverse


def index(request):
    return HttpResponseRedirect(reverse('archive:bg', args=(1,)))


def index_person(request):
    return HttpResponseRedirect(reverse('archive:person', args=(1,)))


def index_bg(request):
    return HttpResponseRedirect(reverse('archive:bg', args=(1,)))


def index_planet(request):
    return HttpResponseRedirect(reverse('archive:planet', args=(1,)))


def index_mission(request):
    return HttpResponseRedirect(reverse('archive:mission', args=(1,)))


def bg(request,pk,state):
    bg_list = BG.objects.all()
    if state == '1':
        bg_list = bg_list.filter(is_active=True)
    elif state == '2':
        bg_list = bg_list.filter(is_active=False)
    if bg_list.filter(pk=pk):
        current_bg = BG.objects.get(pk=pk)
    else:
        current_bg = bg_list.first()
    context = {'BG_list': bg_list,
               'current_bg': current_bg,
               'state': state}
    return render(request, 'archive/bg.html', context)


def person(request,pk,state):
    person_list = Person.objects.all()
    if state == '1':
        person_list = person_list.filter(is_st_nab=True)
    elif state == '2':
        person_list = person_list.filter(is_st_nab=False)
    if person_list.filter(pk=pk):
        current_person = Person.objects.get(pk=pk)
    else:
        current_person = person_list.first()
    context = {'Person_list': person_list,
               'current_person': current_person,
               'state': state}
    return render(request, 'archive/people.html', context)


def planet(request,pk):
    planet_list=Planet.objects.all();
    if planet_list.filter(pk=pk):
        current_planet=Planet.objects.get(pk=pk)
    else:
        current_planet=planet_list.first()
    context = {'Planet_list': planet_list,
               'current_planet': current_planet}
    return render(request, 'archive/planet.html', context)


def mission(request,pk):#
    return render(request, 'archive/mission.html')


def mission_bg(request,pk,state):#state - id боевой группы
    
    mission_list = Mission.objects.all()
    mission_list = mission_list.filter(bg__pk=state)
    BG_list = BG.objects.all()
    
    if mission_list.filter(pk=pk):
        current_mission = Mission.objects.get(pk=pk)
    else:
        current_mission = mission_list.first()
    
    context = {'BG_list': BG_list,
               'Mission_list': mission_list,
               'current_mission': current_mission,
               'state': state}
    return render(request, 'archive/mission_bg.html', context)


def mission_watch(request,pk,state):#state - id боевой группы
    if bg == '0':
        return render(request, 'archive/mission.html')
    mission_list = Mission.objects.all()
    mission_list = mission_list.filter(watch=state)
    if mission_list.filter(pk=pk):
        current_mission = Mission.objects.get(pk=pk)
    else:
        current_mission = mission_list.first()
    
    context = {'Mission_list': mission_list,
               'current_mission': current_mission,
               'state': state}
    return render(request, 'archive/mission_watch.html', context)
