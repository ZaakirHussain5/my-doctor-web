from django.urls import path
from . import views

app_name='doctorsUI'

urlpatterns=[
    path('dashboard',views.dashboard,name='dashboard'),
    path('consultations',views.consultations,name='consultations'),
    path('appointments',views.appointments,name='appointments'),
    path('Prescription', views.Prescription, name="Prescription"),
]