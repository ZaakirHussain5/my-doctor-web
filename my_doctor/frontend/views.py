from django.shortcuts import render
from specialist_type.models import specialist_type

def login(request):
    return render(request,'auth/login.html')

def dashboard(request):
    return render(request,'auth/dashboard.html')

def specialists(request):
    return render(request,'frontend/specialists.html')

def Doctors(request):
    return render(request,'frontend/Doctors.html',{
        "specialist_types":specialist_type.objects.all()
    })

def Executives(request):
    return render(request,'frontend/Executives.html')

def customerCareDashboard(request):
    return render(request,'frontend/customerCareDashboard.html')

def patientsList(request):
    return render(request,'frontend/patientsList.html')

def newAppointment(request):
    return render(request,'frontend/newAppointment.html')