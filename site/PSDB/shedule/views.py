#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, reverse
from .models import Lesson, Watcher
from django.views import generic
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
import archive
from archive.models import Point


def index(request):
    #вернуть когда размораживать проект
    #return HttpResponseRedirect(reverse('shedule:lesson', args=(1,0)))
    context = {
               'user': request.user,
               }
    return render(request, 'shedule/banner.html', context)


def shedule(request, day):
    return HttpResponseRedirect(reverse('shedule:lesson', args=(day,0)))

def lesson (request, day, pk):
    day_list = Lesson.objects.fake_day_list()
    lesson_list = Lesson.objects.day_lessons(day)
    lesson_list_1 = lesson_list.filter(part_time = 1)
    lesson_list_2 = lesson_list.filter(part_time = 2)
    lesson_list_3 = lesson_list.filter(part_time = 3)
    current_lesson = lesson_list.filter(pk=pk).first()
    context = {'lesson_list' : lesson_list,
               'lesson_list_1': lesson_list_1,
               'lesson_list_2': lesson_list_2,
               'lesson_list_3': lesson_list_3,
               'day_list': day_list,
               'user': request.user,
               'current_lesson': current_lesson,}
    return render(request, 'shedule/shedule.html', context)

def mk(request):
    user = request.user
    watcher = user.watcher
    lesson_list = watcher.student_lessons.all()
    mk_list = lesson_list.filter(students__id=request.user.watcher.pk)
    
    context = {'watcher':watcher,
                'user' : user,
               'mk_list' : mk_list}
    return render(request, 'shedule/mk.html', context)

def mark(request):
    user = request.user
    
    
    mark_list = Point.objects.all()
    mark_list = mark_list.filter(watcher=user.watcher)
    watcher = user.watcher
    context = {'watcher':watcher,
               'user' : user,
               'mark_list' : mark_list}
    return render(request, 'shedule/mark.html', context)

def enroll(request, day,pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    if (request.user.is_authenticated):
        watcher = request.user.watcher
        students = lesson.students.all()
        
        answer = (not students.filter(pk=watcher.pk))
        if (not answer):
            messages.error(request, 'Вы уже записаны на этот МК')
        else:
            part_time = lesson.part_time
            current_hour_lessons = Lesson.objects.filter(day = lesson.day, part_time = part_time)
            answer = True
            for les in current_hour_lessons:
                answer = (answer and (not les.students.filter(pk = watcher.pk)))
            if (not answer):
                messages.error(request, 'Вы уже выбрали мастеркласс в этом часу')
            else:
                answer = (students.count() < lesson.max_students)
		if (answer):
                    if (not lesson.is_specialization):
		        previous_lesson = Lesson.objects.all().filter(name=lesson.name)[:3]
		        if (previous_lesson):
                            answer = True
                            for pr_less in previous_lesson:
		                previous_student = pr_less.students.filter(pk=watcher.pk)
		                if (previous_student):
		                    answer = False
                            if (not answer):
		                messages.error(request, 'Вы не можете записаться на этот МК т.к. уже были на нем')
		else:
		    messages.error(request, 'Все места уже заняты')
		if (answer):
		    lesson.students.add(watcher)
		    lesson.save()
		    messages.success(request, "Готово! Вы записались на это занятие")
    else:
        messages.error(request, 'Войдите в систему, прежде чем записываться')
    return HttpResponseRedirect(reverse('shedule:lesson', args=(lesson.day, pk,)))

def exit(request):
    logout(request)
    return HttpResponseRedirect(reverse('shedule:login'))

def enter(request):
    if (not request.POST):
        return render(request, 'shedule/signin.html')
    else:
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('shedule:lesson', args=(1, 0)))
        else:
             messages.error(request, 'Неверный логин/пароль')
             return render(request, 'shedule/signin.html')

def account(request):
    context = {'watcher':request.user.watcher,
                'user' : request.user,}
    return render(request, 'shedule/account.html', context)

def watcher(request, pk):
    if (pk == request.user.watcher.pk):
        return HttpResponseRedirect(reverse('shedule:account'))
    else:
        watcher = get_object_or_404(Watcher, pk=pk)
        context = {'watcer':watcher,
                   'user':request.user}
        return render(request, 'shedule/account.html', context)

def edit(request):
    if (request.method == 'POST'):
        name = request.POST.get('name')
        bg = request.POST.get('bg')
        info = request.POST.get('info')
        watcher = request.user.watcher
        watcher.name = name
        watcher.bg = bg
        watcher.info = info
        watcher.save()
        return HttpResponseRedirect(reverse('shedule:account'))
    else:
        context = {'watcher': request.user.watcher,
                   'user': request.user, }
    return render(request, 'shedule/edit.html', context)

def points(request, pk):
    user = request.user
    watcher = user.watcher
    mission_list = watcher.missions
    context = {''}
