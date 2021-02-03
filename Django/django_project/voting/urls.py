from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('aquery',views.aquery,name='aquery'),
    path('sort',views.sorte,name='sort')
]