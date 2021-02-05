from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    path('dashboard',views.dashboard,name='dashboard'),
    path('appointments',views.appointments,name='appointments'),
    path('consultations',views.consultations,name='consultations'),
    path('selectDoctors',views.selectDoctors,name='selectDoctors'),
    path('new-appointment',views.newAppointment,name='newAppointment'),
    path('billHistory',views.billHistory,name='billHistory'),
    path('medical-records',views.medical_records,name='medicalRecords'),
    path('plan',views.plan,name='plan'),
    path('invoice',views.invoice,name='invoice'),
    path('patientInvoice/', views.patientInvoice, name='patientInvoice'),
    path('single_prescrption/', views.prescrption, name='single_prescrption'),
    path('lab_tests/', views.labtest, name='lab_tests'),
    path('lab_tests_details/', views.labtest_single, name='lab_tests_details'),
    path('lab_tests_orders/', views.labTestsOrders, name='lab_tests_orders'),
]