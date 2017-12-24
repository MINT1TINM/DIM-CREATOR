# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from DIMCREATOR.public_function import *
from models import *
from Dashboard.models import *
from Home.models import *
from django.db.models import Sum

def login(request):
    if request.method == 'GET':
        try:
            del request.session["username"]
        except:
            pass
        return render(request, 'User/login.html')
    else:
        if request.POST.get('username'):
            username = request.POST['username'].replace(u' ', u'')
            password = request.POST['password'].replace(u' ', u'')
            if antisql(username) or antisql(password):
                return render(request, 'User/login.html', {'notice': '系统错误', 'username': username})

            res = sql_select(
                "select username,role,id from user where username ='%s' and password=AES_ENCRYPT('%s','Piclass520')" % (
                    username, password))
            # username role head 被 select 出来之后赋值给res对象，此时res对象是一个二维数组[[username,role,head],[]...[]]

            if len(res) == 0:
                print "error"
                return render(request, 'User/login.html', {'notice': '用户名或密码错误', 'username': username})
            else:
                request.session['username'] = username
                request.session['role'] = res[0][1]
                request.session['id'] = res[0][2]
                if res[0][1] == '9':
                    return HttpResponseRedirect('../Home/index.html')
                else:
                    return HttpResponseRedirect('../Home/index.html')

        
            
def signup(request):
    if request.method == 'GET':
        try:
            del request.session["username"]
        except:
            pass
        return render(request, 'User/signup.html')
    else:
        if request.POST.get('newusername'):
            newusername = request.POST['newusername']
            newpassword = request.POST['newpassword']
            if antisql(newusername) or antisql(newpassword):
                return HttpResponseRedirect('../User/signup.html?message=error')

            conflict = User.objects.filter(username = newusername).count()
            if conflict == 1:
                return HttpResponseRedirect('../User/signup.html?message=error')

            sql_write(
                "insert into user (username,password,role) values ('%s',AES_ENCRYPT('%s','Piclass520'),'%s')" % (
                    newusername, newpassword, 0))
            res = sql_select(
                "select username,role,id from user where username ='%s' and password=AES_ENCRYPT('%s','Piclass520')" % (
                    newusername, newpassword))
            request.session['username'] = newusername
            request.session['role'] = res[0][1]
            request.session['id'] = res[0][2]
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
    ware = Warehouse.objects.filter(username = user.username).order_by('-workid')
    view = Warehouse.objects.filter(username = user.username).aggregate(Sum('view'))
    viewcal = view['view__sum']
    
    return render(request, 'User/viewprofile.html',{"user":user,"ware":ware,"view":viewcal})