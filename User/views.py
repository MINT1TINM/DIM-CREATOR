# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from DIMCREATOR.public_function import *
from models import *

def login(request):
    if request.method == 'GET':
        try:
            del request.session["username"]
        except:
            pass
        return render(request, 'User/login.html')
    else:
        username = request.POST['username'].replace(u' ', u'')
        password = request.POST['password'].replace(u' ', u'')
        if antisql(username) or antisql(password):
            return render(request, 'User/login.html', {'notice': 'Error!', 'username': username})

        res = sql_select(
                "select username,role,id from user where username ='%s' and password=AES_ENCRYPT('%s','Piclass520')" % (
                    username, password))
        # username role head 被 select 出来之后赋值给res对象，此时res对象是一个二维数组[[username,role,head],[]...[]]

        if len(res) == 0:
            print "success"
            return render(request, 'User/login.html', {'notice': '密码错误', 'username': username})
        else:
            request.session['username'] = username
            request.session['role'] = res[0][1]
            request.session['id'] = res[0][2]
            if res[0][1] == '1':
                return HttpResponseRedirect('../Home/index.html')
            else:
                return HttpResponseRedirect('../Home/index.html')

def profile(request):
    if "username" not in request.session:            
        return render(request, 'User/login.html')
    else:  
        username = request.session['username']
        user = User.objects.get(username = username)
        if request.method == "POST":
            user.phone = request.POST["phone"]
            user.email = request.POST["email"]
            user.age = request.POST["age"]
            user.company = request.POST["company"]
            user.job = request.POST["job"]
            user.description = request.POST["description"]
            user.save()
            return HttpResponseRedirect('../User/profile.html')

        else:
            return render(request, 'User/profile.html',{"user":user})

def viewprofile(request):
    id = request.GET["id"]
    user = User.objects.get(id = id)
    return render(request, 'User/viewprofile.html',{"user":user})