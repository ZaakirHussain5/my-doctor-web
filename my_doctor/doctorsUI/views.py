from django.shortcuts import render

def dashboard(request):
    return render(request,'doctorsUI/dashboard.html')

def consultations(request):
    return render(request,'doctorsUI/consultations.html')

def appointments(request):
    return render(request,'doctorsUI/appointments.html')