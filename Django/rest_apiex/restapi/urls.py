from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('a',views.emp_show),
    path('a',views.emp_view.as_view()),
    path('ud/<int:p>',views.emp_ud)
  ]