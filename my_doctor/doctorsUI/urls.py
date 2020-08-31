from django.urls import path
from . import views

app_name='doctorsUI'

urlpatterns=[
    path('dashboard',views.dashboard,name='dashboard')
]