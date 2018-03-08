"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from os import path
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

from shedule import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^shedule/', include('shedule.urls')),
    url(r'^archive/', include('archive.urls')),
    url(r'^$', views.index),
]
#path.join(path.dirname(path.dirname(path.abspath(__file__))), 'static/')
