from django.urls import path
from . import views

app_name = 'frontend'
urlpatterns=[
    path('',views.login,name='login'),
    path('adminDashboard',views.dashboard,name='adminDashboard'),
    path('specialists',views.specialists,name='specialists'),
    path('newDoctor',views.newDoctor,name='newDoctor'),
    path('doctorsList',views.doctorsList,name='doctorsList'),
    path('newExecutive',views.newExecutive,name='newExecutive'),
    path('executivesList',views.executivesList,name='executivesList'),

]