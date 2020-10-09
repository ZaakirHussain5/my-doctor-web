from django.urls import path, include
from rest_framework import routers
from . import views
from .api import Enquires

router = routers.DefaultRouter()

app_name = 'frontend'
urlpatterns=[
    path('app-login',views.login,name='login'), #<str:type>
    path('adminDashboard',views.dashboard,name='adminDashboard'),
    path('specialists',views.specialists,name='specialists'),
    path('Doctors',views.Doctors,name='Doctors'),
    path('Executives',views.Executives,name='Executives'),
    path('enquiresList', views.EnquiresList,  name="enquiresList"),
    path('customerCareDashboard',views.customerCareDashboard,name='customerCareDashboard'),
    path('patientsList',views.patientsList,name='patientsList'),
    path('newAppointment',views.newAppointment,name='newAppointment'),
    path('consultationsList', views.consultationsList, name="consultations_list"),
    path("WebDoctorList", views.webDoctorList, name="webDoctorList"),
    path('getAllCount', views.GetAllInfoCount, name="GetMyAllInfo"),
    path('viewDoctorPayments', views.viewDoctorPayment, name="viewDoctorPayment"),
    path('reminders', views.reminders, name="reminders"),
    path('searching', Enquires, name="searching")

]