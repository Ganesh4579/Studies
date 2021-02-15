from django.urls import path
from . import views

urlpatterns = [
    path('ut',views.home, name='home'),
]