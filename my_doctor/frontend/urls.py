from django.urls import path, include
from rest_framework import routers
from . import views
from .api import SearchAPI

router = routers.DefaultRouter()

app_name = 'frontend'

urlpatterns=[
    path('app-login',views.login,name='login'), #<str:type>
    path('adminDashboard',views.dashboard,name='adminDashboard'),
    path('specialists',views.specialists,name='specialists'),
    path('AddNewDoctor',views.Doctors,name='Doctors'),
    path('DoctorLists',views.DoctorsLists,name='doctor_list'),
    path('DoctorInfo/<id>',views.doctor_info,name='doctor_info'),
    path('Executives',views.Executives,name='Executives'),
    path('enquiresList', views.EnquiresList,  name="enquiresList"),
    path('NewPatient',views.customerCareDashboard,name='customerCareDashboard'),
    path('patientsList',views.patientsList,name='patientsList'),
    path('newAppointment',views.newAppointment,name='newAppointment'),
    path('consultationsList', views.consultationsList, name="consultations_list"),
    path("WebDoctorList", views.webDoctorList, name="webDoctorList"),
    path('getAllCount', views.GetAllInfoCount, name="GetMyAllInfo"),
    path('viewDoctorPayments', views.viewDoctorPayment, name="viewDoctorPayments"),
    path('reminders', views.reminders, name="reminders"),
    path('subscription_plans', views.subscription_plans, name="subscription_plans"),
    path('searchAPI', SearchAPI, name="searchAPI"),
    path('doctorAgreement', views.doctorAgreement, name="doctorAgreement"),
    path('doctorBankDetails', views.doctorBankDetails, name="doctorBankDetails"),
    path('doctorTimings', views.doctorTimings, name="doctorTimings"),
    path('doctorBillPayments', views.doctorBillPayments, name="doctorBillPayments"),
    path('Prescription', views.prescription, name="Prescription"),
    path('search',views.searchUI,name="search"),
    path('mis_reports',views.mis_reports,name="mis_reports"),
    path('appointments',views.appointments,name="appointments"),
    path('patientDetails/<id>', views.patients_details, name="patient_details"),
    
]