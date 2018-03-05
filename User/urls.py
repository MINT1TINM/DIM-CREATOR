from django.conf.urls import url,include
from django.contrib import admin
from views import *
import User.views

urlpatterns = [
    url(r'^login.html$', login),
    url(r'^signup.html$', signup),
    url(r'^profile.html$', profile),
    url(r'^viewprofile.html$', viewprofile),

    url(r'^follow', User.views.follow, name='follow'),    
]
