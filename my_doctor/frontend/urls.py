from django.urls import path, include
from rest_framework import routers
from . import views
from .api import SearchAPI, snap_shots

router = routers.DefaultRouter()

app_name = 'frontend'

urlpatterns=[
    path('adminlogin',views.loginView,name='loginAdmin'), #<str:type>
    path('admin/',views.dashboard,name='adminDashboard'),
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
    path('labtests', views.labtests, name="labtests"),
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
    path('getSnapshots', snap_shots, name="getSnapshots"),
    path('promo_code', views.promo_code, name="promoCode"),
    path('logout-stuff/', views.loutoutView, name="logoutStuffs"),
    path('Manage_lab_test_packages', views.lab_Tests_packages, name="Manage_lab_test_packages"),
    path('labtest_perches', views.labTest_perches, name="labtest_perches"),
    path('labtest_perches/<id>/', views.purches_files, name="purches_file"),
]