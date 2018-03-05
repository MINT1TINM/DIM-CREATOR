# coding=utf-8
from django.shortcuts import render
import json
import requests
from django.http import HttpResponse, HttpResponseRedirect
from Dashboard.models import *
from Home.models import *
from DIMCREATOR.public_function import *
import collections
import datetime
import os
import shutil
from django.core.paginator import Paginator

def useranalysis(request):
    return render(request,"Analysis/useranalysis.html")

def wareanalysis(request):
    return render(request,"Analysis/wareanalysis.html")