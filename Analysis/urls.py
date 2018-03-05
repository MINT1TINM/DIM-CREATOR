from django.conf.urls import url,include
from django.contrib import admin
from views import *
import Analysis.views


urlpatterns = [
    url(r'^useranalysis.html$', useranalysis),
    url(r'^wareanalysis.html$', wareanalysis),
]
