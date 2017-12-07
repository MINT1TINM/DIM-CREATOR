from django.conf.urls import url,include
from django.contrib import admin
from views import *
import Dashboard.views

urlpatterns = [
    url(r'^index.html$', index),
    url(r'^warehouse.html$', warehouse),
    url(r'^ware.html$', ware),
    url(r'^shelf.html$', shelf),
    
]
