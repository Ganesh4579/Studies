from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


# Create your views here.

def func1(request):
    return HttpResponse('<h1>HOME PAGE</h1>')

def rnd(request):
    return render(request,'in.html')

def rnd1(request):
    return render(request,'in1.html')

def rnd2(request):
    a='Hello'
    b='Man'
    l=list('abcdefghijklmnopqrstuvwxyz')
    n1,n2=5,7
    ans=n1 > n2
        
    mydick={
        'a' : a,
        'b' : b,
        'lf' : l,
        'n1' : n1,
        'n2' : n2,
        'ans' :ans
    }
    return render(request,'in2.html',context=mydick)

def img(request):
    return render(request,'img.html')

def img1(request,ina):
    imgname =str(ina)
    imgname=imgname.lower()
    ans= True if imgname == 'image1' else False
    mydict ={
        'img' : imgname,
        'ans' : ans
    }
    return render(request,'img1.html',context=mydict)

def form1(request):
    return render(request,'form1.html')

def fget(request):
    md={
        'method': request.method,
        "Email" : request.GET['email'],
        "pwd" : request.GET['pwd']
    }
    return JsonResponse(md)

def fpost(request):
    md={
        'method': request.method,
        "Email" : request.POST['email'],
        "pwd" : request.POST['pwd']
    }
    return JsonResponse(md)

from . form1 import *
def dform(request):
    if request.method == 'POST':
        form=exform(request.POST)
        if form.is_valid():
            return HttpResponse(str("form submitted" +str(request.method)))
        else:
             dic={
            'fo': form
        }
        return render(request,'dform.html',context=dic)
    elif request.method =='GET':
        form=exform()
        dic={
            'fo': form
        }
        return render(request,'dform.html',context=dic)
    
def dform1(request):
    if request.method == 'POST':
        form=exform(request.POST)
        if form.is_valid():
            dic={
                'fo': form
            }
            if request.POST['Name'].isupper():
                dic['c']=True
                dic['s']='Form got submitted'
                return render(request,'dform.html',context=dic)
            else:
                dic['w']=True
                dic['e']='Name must be in uppercase'
                return render(request,'dform.html',context=dic)
                 
        else:
             dic={
            'fo': form
        }
        return render(request,'dform.html',context=dic)
    else:
        form=exform()
        dic={
            'fo': form
        }
        return render(request,'dform.html',context=dic)
    
from . form2 import *
import re
def dform2(request):
    if request.method == 'POST':
        form=exform1(request.POST)
        if form.is_valid():
            dic={
                'fo': form
            }
            err=list()
            ef=False
            if not request.POST['Name'].isupper():
                ef=True
                err.append('Name must be in upper case')
                dic['l']=err
                dic['ef']=ef
                
            if not re.search(request.POST['Email'],'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'):
                ef=True
                err.append('Enter valid email')
                dic['l']=err
                dic['ef']=ef
                
            if  ef==False:
                dic['c']=True
                dic['s']='Form got submitted'
                return render(request,'dform.html',context=dic)
            else:
                return render(request,'dform.html',context=dic)
                 
        else:
             dic={
            'fo': form
        }
        return render(request,'dform1.html',context=dic)
    else:
        form=exform1()
        dic={
            'fo': form
        }
        return render(request,'dform1.html',context=dic)
    
def n404(request,exception):
    return render(request,'404.html')
    
from . import models

def dbcon(request,emp_ID):
    return HttpResponse('emp_ID :'+str(emp_ID))