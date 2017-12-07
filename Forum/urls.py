from django.conf.urls import url,include
from django.contrib import admin
from views import *
import Forum.views

urlpatterns = [
    url(r'^index.html$', index),
    
]
