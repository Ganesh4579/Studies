from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('/<int:ID>',views.home2,name='home2'),
    path('/insert',views.insertd,name='insert')
]