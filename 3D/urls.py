from django.conf.urls import url,include
from django.contrib import admin
from views import *

urlpatterns = [
    url(r'^editor.html$', editor),
    url(r'^explorer.html$',explorer)
]
