from django.shortcuts import render
from patients.models import patient_info
def dashboard(request):
    return render(request,'doctorsUI/dashboard.html')

def consultations(request):
    return render(request,'doctorsUI/consultations.html')

def appointments(request):
    return render(request,'doctorsUI/appointments.html')

def Prescription(request):
	context ={}
	patients = patient_info.objects.all()
	context['patients'] = patients
	return render(request, 'doctorsUI/prescription.html', context)

def profile(request):
	return render(request,'doctorsUI/profile.html')

def settings(request):
	return render(request,'doctorsUI/settings.html')