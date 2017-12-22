from django.shortcuts import render
from Dashboard.models import Warehouse


def editor(request):
    return render(request, "3D/editor.html")

def explorer(request):
    workid = request.GET["workid"]
    ware = Warehouse.objects.get(workid=workid)
    title = ware.title
    author = ware.username.username
    type = ware.type
    description = ware.description
    
    status = ware.status
    if status == 0:   
        if request.session["username"] == ware.username.username:
            return render(request, "3D/explorer.html",{"workid":workid,"title":title,"author":author,"type":type,"description":description})
        else:
            return render(request, 'User/login.html')
    else:   
        return render(request, "3D/explorer.html",{"workid":workid,"title":title,"author":author,"type":type,"description":description})

def explorer2(request):
    workid = request.GET["workid"]
    return render(request, "3D/explorer2.html",{"workid":workid})

