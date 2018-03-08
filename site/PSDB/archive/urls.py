from django.conf.urls import url
from . import views

app_name = 'archive'

urlpatterns = [
    url(r'^$', views.index, name='archive'),
    url(r'^person/$', views.index_person, name='index_person'),
    url(r'^bg/$', views.index_bg, name='index_bg'),
    url(r'^planet/$', views.index_planet, name='index_planet'),
    url(r'^planet/(?P<pk>[0-9]+)/$', views.planet, name='planet'),
    url(r'^mission/(?P<pk>[0-9]+)/$', views.mission, name='mission'),
    url(r'^person/(?P<pk>[0-9]+)/(?P<state>[0-9]+)/$', views.person, name='person'),
    url(r'^bg/(?P<pk>[0-9]+)/(?P<state>[0-9]+)/$', views.bg, name='bg'),
    url(r'^mission/(?P<pk>[0-9]+)/bg/(?P<state>[0-9]+)/$', views.mission_bg, name='mission_bg'),
    url(r'^mission/(?P<pk>[0-9]+)/watch/(?P<state>[0-9]+)/$', views.mission_watch, name='mission_watch'),
    ]
