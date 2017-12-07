"""DIMCREATOR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
# coding=utf-8
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.shortcuts import render
import settings
import os
from Dashboard.models import Warehouse
import json
import requests
from django.http import HttpResponse, HttpResponseRedirect
from DIMCREATOR.public_function import *
import collections
import datetime
from django.core.paginator import Paginator


def index(request):
    try:
        del request.session["username"]
    except:
        pass
    ware = Warehouse.objects.filter( status = 1 ).order_by('-workid')       
    paginator=Paginator(ware, 6) 
    page = request.GET.get('page','1')
    ware = paginator.page(page)
    return render(request, "Home/index.html" ,{"ware":ware})

urlpatterns = [
    url(r'^$', index),
    url(r'^Home/', include('Home.urls')),
    url(r'^User/', include('User.urls')),
    url(r'^Dashboard/', include('Dashboard.urls')),
    url(r'^3D/', include('3D.urls')),
    url(r'^Forum/', include('Forum.urls')),    
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT },name='static'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT },name='media'),
]
