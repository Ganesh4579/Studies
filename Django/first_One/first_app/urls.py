from django.urls import path
from . import views

urlpatterns = [
    path('',views.func1,name='func1'),
    path('rnd',views.rnd,name='rnd'),
    path('rnd1',views.rnd1,name='rnd1'),
    path('rnd2',views.rnd2,name='rnd2'),
    path('img',views.img,name='img')
]