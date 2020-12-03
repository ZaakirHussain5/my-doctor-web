from django.shortcuts import render
from patients.models import patient_info
from consultations.models import consultations


def dashboard(request):
    return render(request,'doctorsUI/dashboard.html')

def consultationsView(request):
    return render(request,'doctorsUI/consultations.html')

def appointmentsView(request):
    return render(request,'doctorsUI/appointments.html')

def Prescription(request):
	context ={}
	pat_id = request.GET.get('pat_id')
	patients = patient_info.objects.all()
	for patient in patients:
		if consultations.objects.filter(patient = patient.user).count() <= 0:
			patients = patients.exclude(id__in = [patient.id])



	context['select_required'] = False
	if pat_id:
		patients = patient_info.objects.filter(id=pat_id)
		context['select_required'] = True
	context['patients'] = patients
	return render(request, 'doctorsUI/prescription.html', context)

def profile(request):
	return render(request,'doctorsUI/profile.html')

def settings(request):
	return render(request,'doctorsUI/settings.html')