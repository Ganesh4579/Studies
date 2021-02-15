from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import employee
from .serializer import empser

# for read and create


@csrf_exempt  # for post
def eeeeemp_show(request):  # changed
    if request.method == 'GET':
        m = employee.objects.all()
        s = empser(m, many=True)
        return JsonResponse(s.data, safe=False)
    elif request.method == 'POST':
        p = JSONParser().parse(request)
        s = empser(employee, data=p)

        if s.is_valid():
            s.save()
            return JsonResponse(s.data, status=201)
        return JsonResponse(s.errors, status=400)


# for read and create using api_view dec

@api_view(["GET", "POST"])
def emp_show(request):
    if request.method == 'GET':
        m = employee.objects.all()
        s = empser(m, many=True)
        return Response(s.data)
    elif request.method == 'POST':
        p = JSONParser().parse(request)
        s = empser(employee, data=p)

        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


# for update and delete
@csrf_exempt
def emp_ud(request, p):
    try:
        a = employee.objects.get(pk=p)
    except employee.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        s = empser(a)
        return JsonResponse(s.data, safe=False)

    elif request.method == 'PUT':
        p = JSONParser().parse(request)
        s = empser(employee, data=p)

        if s.is_valid():
            s.save()
            return JsonResponse(s.data, status=201)
        return JsonResponse(s.errors, status=400)

    elif request.method == 'DELETE':
        a.delete()
        return HttpResponse(status=204)


# clss based api view


class emp_view(APIView):
    def get(self, request):
        m = employee.objects.all()
        s = empser(m, many=True)
        return Response(s.data)

    def post(self, request):
        p = JSONParser().parse(request)
        s = empser(employee, data=p)

        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


# generic api_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
    
class emp_gv(generics.GenericAPIView, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):  # ther are more mixins
    
    serializer_class = empser
    queryset = employee.objects.all()

    lookup_fields = 'id'
    
    #authentication purpose
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrive(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)
