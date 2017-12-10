# coding=utf-8
from django.shortcuts import render
import json
import requests
from django.http import HttpResponse, HttpResponseRedirect

from Dashboard.models import Warehouse
from User.models import User
from Home.models import *

from DIMCREATOR.public_function import *
import collections
import datetime
import os

from django.db.models import Q

def index(request):
    return render(request, "Forum/index.html")
