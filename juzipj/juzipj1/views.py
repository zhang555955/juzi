from django.shortcuts import render,HttpResponse

# Create your views here.

import time

def ntime(req):

    t = time.ctime()

    return render(req,"index.html",{'time':t})

def year(req,y):
    print(y)
    return HttpResponse(str(y)+"年")

def month(req,y,m):
    return HttpResponse(str(y)+"年"+str(m)+"月")

def days(req,year,month):
    return HttpResponse(str(year)+"年"+str(month)+"月")

def register(req):
    print(req.GET.get("user"))
    print(req.GET.get("age"))
    return render(req,"register.html")