# -*- coding: utf-8 -*-
import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render
from .models import BG
from .models import Planet
from .models import Person
from .models import Mission
from .models import Challenge
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
    info_list = current_bg.info.split("\n")
    context = {'BG_list': bg_list,
           'current_bg': current_bg,
           'state': state,
           'info_list': info_list}
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
    info_list = current_person.career.split("\n")
    work_list = current_person.work_before.split("\n")
    edu_list = current_person.education.split("\n")
    context = {'Person_list': person_list,
               'current_person': current_person,
               'state': state,
               'info_list': info_list,
               'work_list': work_list,
               'edu_list': edu_list}
    return render(request, 'archive/people.html', context)


def planet(request,pk):
    planet_list=Planet.objects.all();
    if planet_list.filter(pk=pk):
        current_planet=Planet.objects.get(pk=pk)
    else:
        current_planet=planet_list.first()
    info_list = current_planet.info.split("\n")
    context = {'Planet_list': planet_list,
               'current_planet': current_planet,
               'info_list': info_list}
    return render(request, 'archive/planet.html', context)


def mission(request,pk):#
    return render(request, 'archive/mission.html')


def mission_bg(request,pk,state):#state - id боевой группы
    
    mission_list = Mission.objects.all()
    mission_list = mission_list.filter(bg__pk=state)
    bg_list=BG.objects.all()
    if not mission_list:
        mission_list=Mission.objects.filter(bg__pk=bg_list[0].pk)
    
    if mission_list.filter(pk=pk):
        current_mission = Mission.objects.get(pk=pk)
    else:
        current_mission = mission_list.first()

    if current_mission:
        target_list = current_mission.target.split("\n")
        info_list = current_mission.info.split("\n")
        BG_list = current_mission.bg.all()
        Planet_list = current_mission.planet.all()
    else:
        target_list = list()
        info_list = list()
        BG_list = list()
        Planet_list = list()
    
    context = {'BGs': bg_list,
               'target_list': target_list,
               'info_list': info_list,
               'BG_list': BG_list,
               'Planet_list': Planet_list,
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

    target_list = current_mission.target.split("\n")
    info_list = current_mission.info.split("\n")
    BG_list = current_mission.bg.all()
    Planet_list = current_mission.planet.all()
    Watch_list = Mission.objects.all().order_by('watch').values_list('watch', flat=True).distinct()
    
    context = {'BG_list': BG_list,
               'info_list': info_list,
               'target_list': target_list,
               'Planet_list': Planet_list,
               'Watch_list': Watch_list,
               'Mission_list': mission_list,
               'current_mission': current_mission,
               'state': state}
    return render(request, 'archive/mission_watch.html', context)

def challenge(request, day, pk):
    day_list = Challenge.objects.all().order_by('date').values_list('date', flat=True).distinct()
    if day:
        challenge_list = Challenge.objects.filter(date=day)
    else:
        challenge_list = Challenge.objects.filter(date=int(datetime.date.today().day))
    challenge_list_1 = challenge_list.filter(level=1)
    challenge_list_2 = challenge_list.filter(level=2)
    if challenge_list.filter(pk=pk):
        current_challenge = Challenge.objects.get(pk=pk)

    else:
        current_challenge = Challenge.objects.all().first()
    nabs_list = current_challenge.nabs.all()

    context = {'challenge_list' : challenge_list,
               'challenge_list_1': challenge_list_1,
               'challenge_list_2': challenge_list_2,
               'day_list': day_list,
               'nabs_list': nabs_list,
               'user': request.user,
               'current_challenge': current_challenge,}
    return render(request, 'archive/challenges.html', context)


def enroll(request, day, pk):
    challenge = get_object_or_404(Challenge, pk=pk)
    if (request.user.is_authenticated):
        watcher = request.user.watcher
        students = challenge.nabs.all()

        answer = (not watcher in students)
        if (not answer):
            messages.error(request, 'Вы уже записаны на этот МК')
        else:
            answer = False
            if challenge.level==1:
                for challenge in Challenge.objects.exclude(level=1):
                    if watcher in challenge.nabs.all():
                        answer = True
            else:
                for challenge in Challenge.objects.exclude(level=2):
                    if watcher in challenge.nabs.all():
                        answer = True
            if answer:
                messages.error(request, 'Вы уже выбрали непростое задание')
            else:
                challenge.nabs.add(watcher)
                challenge.save()
                messages.success(request, "Готово! Вы записались на это занятие")
    else:
        messages.error(request, 'Войдите в систему, прежде чем записываться')
    return HttpResponseRedirect(reverse('archive:challenge', args=(day, pk,)))

