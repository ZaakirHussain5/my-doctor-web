from django.urls import path
from .import views

app_name='website'

urlpatterns = [
    path('',views.index,name='index'),
    path('features',views.features,name='features'),
    path('specialty',views.specialty,name='specialty'),
    path('plans',views.plans,name='plans'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('login',views.login,name='login'),
    path('contact',views.contact,name='contact'),
    path('terms_condition',views.terms_condition,name='terms_condition'),
    path('privacy_policy',views.privacy_policy,name='privacy_policy'),
    path('faq',views.faq,name='faq'),
    path('doctor_reg',views.doctor_reg,name='doctor_reg'),
    path('forgot_pass',views.forgot_pass,name='forgot_pass'),
]