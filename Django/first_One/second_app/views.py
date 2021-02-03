from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,Http404
from django.template import loader

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . models import employee,branch
from . import form
from . serializer import *

emp=employee.objects.all()
branch=branch.objects.all()

# For API

class getemployees(APIView):
    def get(self,request):
        emp1=emp
        s=employeeSerializer(emp1,many=True)
        return Response(s.data)
    
    def post(self,request):
        pass
    


# Create your views here.

def home(request):
    temp=loader.get_template('/mnt/223658B236588925/Studies/Programs/Django/first_One/second_app/templates/second_app/home.html')
    c={
        'emp': emp
    }
    return HttpResponse(temp.render(c,request))

def home2(request,ID):
    try:
        s=str(models.employee.objects.get(emp_ID=ID))
        b=models.branch.objects.get(pk=ID)
    except models.employee.DoesNotExist:
        raise Http404(r'Does not Exist')
    dic={
        's':s,
        'b':b.branch_name
    }
    return render(request,'/mnt/223658B236588925/Studies/Programs/Django/first_One/second_app/templates/home2.html',context=dic)

def insertd(request):
    f=False
    fo=form.getval1(request.POST)
    if request.method == 'POST':
        if fo.is_valid():
            e=models.employee()
            b=models.branch()
            e.emp_ID=fo.cleaned_data['ID']
            e.emp_name=request.POST['name']
            #b.emp_nu=
            b.branch_name=request.POST['branch_name']
            e.save()
            b.save()
            f=True
            dic={
            'fo': fo,
            'f':f
            }
            return render(request,'/mnt/223658B236588925/Studies/Programs/Django/first_One/second_app/templates/second_app/insert.html',context=dic)
        else:
            dic={
            'fo': fo,
            'f':f
        }
        return render(request,'/mnt/223658B236588925/Studies/Programs/Django/first_One/second_app/templates/second_app/insert.html',context=dic)
    else:
        dic={
            'fo': fo,
             'f':f
        }
        return render(request,'/mnt/223658B236588925/Studies/Programs/Django/first_One/second_app/templates/second_app/insert.html',context=dic)