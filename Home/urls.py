from django.conf.urls import url,include
from django.contrib import admin
from views import *
import Home.views

urlpatterns = [
    url(r'^index.html$', index),
    url(r'^collection.html$', collection),
    url(r'^collection-single.html$', collectionsingle),
    url(r'^explore.html$', explore),
    url(r'^exploreresult.html$', exploreresult),
    url(r'^about.html$', about),
    url(r'^like/$', 'Home.views.like', name='like'),    
    
]
