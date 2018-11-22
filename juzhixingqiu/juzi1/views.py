from django.shortcuts import render,HttpResponse

# Create your views here.

import datetime
from juzi1 import models

def time(request):
    now_t = datetime.datetime.now()

    return render(request,"xs_time.html",{"time": now_t})#第一个参数request,第二个参数返回到页面，第三个参数显示什么。

def reg(request):
    if request.method == "POST":
        uname = request.POST.get("username",None)
        upawd = request.POST.get("password",None)
        #print(uname,upawd)
        models.Userinfo.objects.create(
            username=uname,
            password=upawd,
        )

    return render(request,"register.html")

