# coding=utf-8
from django.shortcuts import render
import json
import requests
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError

from Dashboard.models import Warehouse
from User.models import User
from models import *

from DIMCREATOR.public_function import *
import collections
import datetime
import os
from django.core.paginator import Paginator
from django.db.models import Q

import qrcode  #二维码模块 pip install qrcode
from PIL import Image  #图像处理 pip install pillow
Image.LOAD_TRUNCATED_IMAGES = True

def index(request):
    ware = Warehouse.objects.filter( status = 1 ).order_by('-workid')       
    paginator=Paginator(ware, 6) 
    page = request.GET.get('page','1')
    ware = paginator.page(page)
    return render(request, "Home/index.html" ,{"ware":ware})

def collection(request):
    ware = Warehouse.objects.filter( status = 1 ).order_by('-workid')        
    return render(request, "Home/collection.html" ,{"ware":ware})

def collectionsingle(request):
    workid = request.GET["workid"]
    ware = Warehouse.objects.get(workid=workid)
    comment = Comment_Product.objects.filter( workid = workid ).order_by('-id')
    comment_count = comment.count()
    ware.view +=1
    ware.save()
    if "username" not in request.session: 
        iliked = 0
        View_Product.objects.create(
            username = 'Tourist',
            workid = Warehouse.objects.get(workid = workid),
            host = Warehouse.objects.get(workid = workid).username.username
        )
    else: 
        iliked = Like_Product.objects.filter(workid = workid, username = request.session["username"]).count()
        View_Product.objects.create(
            username = User.objects.get(username = request.session["username"]).username,
            workid = Warehouse.objects.get(workid = workid),
            host = Warehouse.objects.get(workid = workid).username.username
        )

    liked = Like_Product.objects.filter(workid = workid).count()
    
    if ware.status == 1:
        if request.method == "POST":
            content = request.POST["comment"]
            time = datetime.datetime.now()  
            Comment_Product.objects.create(
                username = User.objects.get(username = request.session["username"]),
                content = content,
                time = str(time.year) + '/' + str(time.month) + '/' + str(time.day),
                workid = Warehouse.objects.get(workid = workid),
                host = Warehouse.objects.get(workid = workid).username.username
            )      

            return HttpResponseRedirect('/Home/collection-single.html?workid=%s'%workid)
        else:
            return render(request, "Home/collection-single.html" ,{"ware":ware,"comment":comment,"comment_count":comment_count,"iliked":iliked,"liked":liked})
    else:
        HttpResponseServerError()


def explore(request):
    return render(request, "Home/explore.html")

def exploreresult(request):
    if request.method == "POST":
        search = request.POST["search"]
        my_filter = Q()
        my_filter = my_filter | Q(title__icontains = search)
        my_filter = my_filter | Q(description__icontains = search)
        my_filter = my_filter | Q(username__username__icontains = search)
        my_filter = my_filter & Q(status = 1)
        ware = Warehouse.objects.filter(my_filter)

        my_filter2 = Q()
        my_filter2 = my_filter2 | Q(username__icontains = search)

        user = User.objects.filter(my_filter2)
        return render(request, "Home/exploreresult.html",{"ware":ware,"user":user})
    else:
        return render(request, "Home/exploreresult.html")

def about(request):
    return render(request, "Home/about.html")


from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def like(request):
    if "username" not in request.session:            
        return render(request, 'User/login.html')
    else: 
        workid = json.loads(request.POST["workid"])
        ware = Warehouse.objects.get(workid=workid)        
        liked = Like_Product.objects.filter(workid = workid, username = request.session["username"]).count()
        if liked >= 1:
            ware.like -= 1
            ware.save()
            delete_like = Like_Product.objects.get(workid = workid, username = request.session["username"])
            delete_like.delete()
            like = {}
            like["result"] = "unlike"
        elif liked == 0:
            ware.like += 1
            ware.save()
            Like_Product.objects.create(
                username = User.objects.get(username = request.session["username"]),
                workid = Warehouse.objects.get(workid = workid),
                host = Warehouse.objects.get(workid = workid).username.username
            )
            like = {}
            like["result"] = "like"
        like["count"] = ware.like
        return HttpResponse(json.dumps(like), content_type='application/json')
    
