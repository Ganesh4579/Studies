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