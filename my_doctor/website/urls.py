from django.urls import path
from .import views

app_name='website'

urlpatterns = [
    path('',views.index,name='index'),
    path('howitworks',views.features,name='features'),
    path('plans',views.plans,name='plans'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('login/',views.login,name='login'),
    path('contact',views.contact,name='contact'),
    path('termsandcondition',views.terms_condition,name='terms_condition'),
    path('privacypolicy',views.privacy_policy,name='privacy_policy'),
    path('faq',views.faq,name='faq'),
    path('DoctorRegistration',views.doctor_reg,name='doctor_reg'),
    path('ForgotPassword',views.forgot_pass,name='forgot_pass'),
    path('PatientRegistration',views.PatientRegistration,name='PatientRegistration'),
    path('doctors_mou_tc',views.doctor_mou_tc,name='doctors_mou_tc'),
    path('lab_tests',views.lab_tests,name='lab_tests'),
    path('lab_test/<id>/', views.detail_lab_test, name="detail_lab_test"),
    path('speciality/generalPhysician', views.spl_gp, name="generalPhysician"),
    path('speciality/Dermatology', views.spl_dermat, name="Dermatology"),
    path('speciality/Pediatrician', views.spl_pt, name="Pediatrician"),
    path('speciality/Dietitian', views.spl_dietitian, name="Dietitian"),
    path('speciality/Ayurveda', views.spl_ayur, name="Ayurveda"),
    path('speciality/Gynaecology', views.spl_gyna, name="Gynaecology"),
    path('speciality/Orthopadic', views.spl_ortho, name="Orthopadic"),
    path('speciality/ENT', views.spl_ent, name="ENT"),
    path('speciality/Gastroentrology', views.spl_gastro, name="Gastroentrology"),
]