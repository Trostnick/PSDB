from django.conf.urls import url
from . import views

app_name = 'shedule'

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^login/$', views.enter, name = 'login'),
    url(r'^exit/$', views.exit, name = 'logout'),
    url(r'^(?P<day>[0-9]+)/$', views.shedule, name='shedule'),
    url(r'^(?P<day>[0-9]+)/(?P<pk>[0-9]+)/$', views.lesson, name='lesson'),
    url(r'^(?P<day>[0-9]+)/(?P<pk>[0-9]+)/enroll/$', views.enroll, name='enroll'),
    url(r'^account/$', views.account, name ='account'),
    url(r'^account/edit/$', views.edit, name='edit'),
    url(r'^account/mk/$', views.mk, name='mk'),
    url(r'^account/mark/$', views.mark, name='mark'),
    url(r'^watcher/(?P<pk>[0-9]+)/$', views.watcher, name='watcher'),
]
