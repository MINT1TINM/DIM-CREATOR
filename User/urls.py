from django.conf.urls import url,include
from django.contrib import admin
from views import *

urlpatterns = [
    url(r'^login.html$', login),
    url(r'^signup.html$', signup),
    url(r'^profile.html$', profile),
]
