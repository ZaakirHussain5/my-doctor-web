from django.urls import path
from . import views

app_name = 'frontend'
urlpatterns=[
    path('app-login',views.login,name='login'), #<str:type>
    path('adminDashboard',views.dashboard,name='adminDashboard'),
    path('specialists',views.specialists,name='specialists'),
    path('Doctors',views.Doctors,name='Doctors'),
    path('Executives',views.Executives,name='Executives'),
    path('customerCareDashboard',views.customerCareDashboard,name='customerCareDashboard'),
    path('patientsList',views.patientsList,name='patientsList'),
    path('newAppointment',views.newAppointment,name='newAppointment'),
    path('consultationsList', views.consultationsList, name="consultations_list")

]