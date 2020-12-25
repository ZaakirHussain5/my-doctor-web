from django.shortcuts import render,redirect
from patients.models import patient_info
from consultations.models import consultations
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def dashboard(request):
    return render(request,'doctorsUI/dashboard.html')

@login_required(login_url='/login')
def consultationsView(request):
    return render(request,'doctorsUI/consultations.html')

@login_required(login_url='/login')
def appointmentsView(request):
    return render(request,'doctorsUI/appointments.html')

@login_required(login_url='/login')
def Prescription(request):
	context ={}
	pat_id = request.GET.get('pat_id')
	patients = patient_info.objects.all()
	for patient in patients:
		if consultations.objects.filter(patient = patient.user).count() <= 0:
			patients = patients.exclude(id__in = [patient.id])
	context['select_required'] = False
	context['consulataion_id'] = 0
	if pat_id:
		patients = patient_info.objects.filter(id=pat_id)
		context['select_required'] = True
		context['consulataion_id'] = request.GET.get('cons_id')
		if context['consulataion_id'] == '':
			return redirect('/doctors/dashboard')
	context['patients'] = patients
	return render(request, 'doctorsUI/prescription.html', context)

@login_required(login_url='/login')
def profile(request):
	return render(request,'doctorsUI/profile.html')

@login_required(login_url='/login')
def settings(request):
	return render(request,'doctorsUI/settings.html')