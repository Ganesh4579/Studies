from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def home(request):
    return render(request, 'home.html')


def sq(request):
    try:
        ans = eval(request.GET['query'])
        dic = {
            'ans': ans,
            'q': request.GET['query'],
            'e': False,
            'r':True
        }

    except:
        dic = {
            'e': True,
            'r':False
        }
    return render(request, 'home.html', context=dic)
