from django.shortcuts import render
from Dashboard.models import Warehouse


def editor(request):
    return render(request, "3D/editor.html")

def explorer(request):
    workid = request.GET["workid"]
    ware = Warehouse.objects.get(workid=workid)
    title = ware.title
    px = ware.px
    py = ware.py
    pz = ware.pz
    
    status = ware.status
    if status == 0:   
        if request.session["username"] == ware.username.username:
            return render(request, "3D/explorer.html",{"workid":workid,"title":title,"px":px,"py":py,"pz":pz})
        else:
            return render(request, 'User/login.html')
    else:   
        return render(request, "3D/explorer.html",{"workid":workid,"title":title,"px":px,"py":py,"pz":pz})

