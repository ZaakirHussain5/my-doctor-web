from django.urls import path
from . import views

app_name='doctorsUI'

urlpatterns=[
    path('dashboard',views.dashboard,name='dashboard'),
    path('consultations',views.consultationsView,name='consultations'),
    path('appointments',views.appointmentsView,name='appointments'),
    path('Prescription', views.Prescription, name="Prescription"),
    path('profile', views.profile, name="profile"),
    path('settings', views.settings, name="settings"),

]