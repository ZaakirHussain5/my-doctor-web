from django.shortcuts import render
from specialist_type.models import specialist_type

def dashboard(request):
    spl_types = specialist_type.objects.all()
    return render(request,'patientsUI/dashboard.html',{
        "specialists":spl_types
    })

def appointments(request):
    return render(request,'patientsUI/appointments.html')

def consultations(request):
    return render(request,'patientsUI/consultations.html')