# coding=utf-8
from django.shortcuts import render
import json
import requests
from django.http import HttpResponse, HttpResponseRedirect
from models import *
from Home.models import *
from DIMCREATOR.public_function import *
import collections
import datetime
import os
import shutil
from django.core.paginator import Paginator

from PIL import Image  #图像处理 pip install pillow
Image.LOAD_TRUNCATED_IMAGES = True

def index(request):
    if "username" not in request.session:            
        return render(request, 'User/login.html')
    else:   
        date = datetime.datetime.now()
        date1 = date + datetime.timedelta(days=-1)
        date2 = date + datetime.timedelta(days=-8)
        now = str(date1.year) + '/' + str(date1.month) + '/' + str(date1.day)
        past = str(date2.year) + '/' + str(date2.month) + '/' + str(date2.day)

        viewcal = View_Product.objects.filter(workid__username = request.session["username"] , time__year=date.year , time__month=date.month , time__day=date.day).count()
        likecal = Like_Product.objects.filter(workid__username = request.session["username"] , time__year=date.year , time__month=date.month , time__day=date.day).count()
        sharecal = Share_Product.objects.filter(workid__username = request.session["username"] , time__year=date.year , time__month=date.month , time__day=date.day).count()

        ware = Warehouse.objects.filter( username = request.session["username"] , status=1 ).order_by('view') 
        paginator=Paginator(ware, 5) 
        page = request.GET.get('page','1')
        most_view_ware = paginator.page(page)

        return render(request, "Dashboard/index.html",{"now":now, "past":past, "viewcal":viewcal, "likecal":likecal, "sharecal":sharecal, "most_view_ware":most_view_ware})

def warehouse(request):

    if "username" not in request.session:            
        return render(request, 'User/login.html')
    else:   

        if request.method == "POST":
            title = request.POST["title"]        

            opendate = datetime.datetime.now()        
            Warehouse.objects.create(username = User.objects.get(username = request.session["username"]),
                                 title = title,
                                 opendate = str(opendate.year) + '/' + str(opendate.month) + '/' + str(opendate.day),
                                 description = "NULL",
                                 view = 0,
                                 like = 0,
                                 share = 0,
                                 cox = 0,
                                 coy = 0,
                                 coz = 0,
                                 cax = 0,
                                 cay = 0,
                                 caz = 0,
                                 status = 0,



            )
            newware = Warehouse.objects.filter(username = request.session["username"]).get(title = title)
            workid = str(newware.workid)

            folderpath = './media/Warehouse/' + workid
            if not os.path.exists(folderpath): 
                os.makedirs(folderpath)
            objpath = "./media/Warehouse/" + workid + "/obj.obj"
            obj = open(objpath, 'wb')
            # obj.write(request.FILES["obj"].read())   不分块
            f = request.FILES['obj']
            for chunk in f.chunks():      # 分块写入文件
                obj.write(chunk)
            obj.close()

            #计算物体中心并存入数据库
            fin = open("./media/Warehouse/" + workid + "/obj.obj","r")
            arr = []
            add_sum = 0
            sum_x,sum_y,sum_z,max_x,max_y,max_z = 0,0,0,0,0,0
            for EachLine in fin:
                if(EachLine[0] == 'v' and EachLine[1] == ' '):
                    data = EachLine.split()
                    sum_x += float(data[1])
                    sum_y += float(data[2])
                    sum_z += float(data[3])
                    max_x = max( abs(float(data[1])),max_x)
                    max_y = max( abs(float(data[2])),max_y)
                    max_z = max( abs(float(data[3])),max_z)
                    arr.append(EachLine)
                    add_sum = add_sum + 1
            fin.close()

            newware.cox = sum_x/add_sum
            newware.coy = sum_y/add_sum
            newware.coz = sum_z/add_sum
            newware.cax = max_x
            newware.cay = max_y
            newware.caz = max_z
            
            newware.save()

        #mtlname = request.FILES['mtl'].name
        #mtlpath = "./media/Warehouse/" + workid + "/mtl.mtl"
        #mtl = open(mtlpath, 'wb')
        #m = request.FILES['mtl']
        #for chunk in m.chunks():
        #    mtl.write(chunk)
        #mtl.close()
           
            jpgname = request.FILES['jpg'].name
            jpgpath = "./media/Warehouse/" + workid + "/jpg.jpg"

            jpg = open(jpgpath, 'wb')

            j = request.FILES['jpg']
            for chunk in j.chunks():
                jpg.write(chunk)
            jpg.close()




            jpg = open(jpgpath)
            size = 700,700
            im = Image.open("./media/Warehouse/" + workid + "/jpg.jpg") 
            im.thumbnail(size)  
            im.save(jpgpath, 'JPEG')
            jpg.close()

            


            return HttpResponseRedirect('../Dashboard/ware.html?workid=%s'%workid)

        else:
            count = Warehouse.objects.filter( username = request.session["username"] ).count()
            ware = Warehouse.objects.filter( username = request.session["username"] ).order_by('-workid')        
            return render(request, "Dashboard/warehouse.html",{"ware":ware,"count":count})



def ware(request):
    
    if "username" not in request.session:            
        return render(request, 'User/login.html')
    else:   
        workid = request.GET["workid"]
        ware = Warehouse.objects.get(workid=workid)
        title = ware.title
        opendate = ware.opendate
        description = ware.description


        if request.method == "POST":
            if request.POST.get('description'):
                newdescription = request.POST["description"]
                ware.description = newdescription
                ware.save()
            if request.POST.get('title'):
                newtitle = request.POST["title"]
                ware.title = newtitle
                ware.save()
            
            return HttpResponseRedirect('../Dashboard/ware.html?workid=%s'%workid)
        else:               
            return render(request, "Dashboard/ware.html",{"workid":workid , "title":title , "opendate":opendate , "description":description})

def shelf(request):
    if "username" not in request.session:            
        return render(request, 'User/login.html')
    else:  
        if request.method == "POST":
            if request.POST.get('up_id'):
                ware = Warehouse.objects.get(workid = request.POST["up_id"])
                ware.status = 1
                ware.save()
            if request.POST.get('down_id'):
                ware = Warehouse.objects.get(workid = request.POST["down_id"])
                ware.status = 0
                ware.save()        
            if request.POST.get('delete_id'):
                delete_id = request.POST["delete_id"]
                ware = Warehouse.objects.get(workid = delete_id)
                shutil.rmtree(r'./media/Warehouse/%s'%delete_id)
                ware.delete()
            return HttpResponseRedirect('../Dashboard/shelf.html')
        else:
            count = Warehouse.objects.filter( username = request.session["username"] , status = 1 ).count()
            ware = Warehouse.objects.filter( username = request.session["username"] ).order_by('-workid')        
            return render(request, "Dashboard/shelf.html",{"ware": ware , "count":count})