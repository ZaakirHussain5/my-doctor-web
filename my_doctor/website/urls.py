from django.urls import path
from .import views

app_name='website'

urlpatterns = [
    path('',views.index,name='index'),
    path('howitworks',views.features,name='features'),
    path('plans',views.plans,name='plans'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('login',views.login,name='login'),
    path('contact',views.contact,name='contact'),
    path('termsandcondition',views.terms_condition,name='terms_condition'),
    path('privacypolicy',views.privacy_policy,name='privacy_policy'),
    path('faq',views.faq,name='faq'),
    path('DoctorRegistration',views.doctor_reg,name='doctor_reg'),
    path('ForgotPassword',views.forgot_pass,name='forgot_pass'),
    path('PatientRegistration',views.PatientRegistration,name='PatientRegistration'),
    path('DoctorsMOU/<id>/',views.doctorsMOU,name='DoctorsMOU'),
]