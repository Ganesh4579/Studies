from django.urls import path
from . import views

urlpatterns = [
    path('',views.func1,name='func1'),
    path('rnd',views.rnd,name='rnd'),
    path('rnd1',views.rnd1,name='rnd1'),
    path('rnd2',views.rnd2,name='rnd2'),
    path('img',views.img,name='img'),
    path("img1/<str:ina>",views.img1,name='img1'),
    path('form',views.form1,name='form1'),
    path('formget',views.fget,name='fget'),
    path('formpost',views.fpost,name='fpost'),
    path('dform',views.dform,name='dform'),
    path('dform1',views.dform1,name='dform1'),
    path('dform2',views.dform2,name='dform2'),
    path('<int:emp_ID>',views.dbcon,name='dbc')
]