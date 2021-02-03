from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='homepage'),
    path('sq',views.sq,name='sq')
]