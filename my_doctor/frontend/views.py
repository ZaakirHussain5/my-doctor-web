from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from specialist_type.models import specialist_type
from patients.models import patient_info
from doctors.models import doctors_info
from consultations.models import consultations

def login(request):
    user_type = ""
    if request.GET.get('user') == 'admin':
        user_type = "A"
    else:
        user_type = "E"
    return render(request,'auth/login.html', context = { "user_type":user_type})

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
    context = {}
    patient_id = request.GET.get('patient')
    print(patient_id)
    patient_data = patient_info.objects.get(id=patient_id)
    print(patient_data)
    context['patient_info'] = patient_data
    return render(request,'frontend/newAppointment.html', context)


def consultationsList(request):
    return render(request, 'frontend/consultationsList.html')

def webDoctorList(request):
    return render(request, 'frontend/doctorsList.html')


def GetAllInfoCount(request):
    registered_doctor = doctors_info.objects.filter(is_active=True).count()
    registered_patients = patient_info.objects.all().count()
    registered_consultations = consultations.objects.all().count()
    obj = {
        'doctorCount': registered_doctor,
        'patientCount': registered_patients,
        'consultationsCount': registered_consultations
    }

    return JsonResponse(obj, safe=False)

def viewDoctorPayment(request):
    return render(request, 'frontend/doctorPaymentsList.html')

def reminders(request):
    return render(request,'frontend/reminders.html')


def EnquiresList(request):
    return render(request, 'frontend/enquiresList.html')

def subscription_plans(request):
    return render(request, 'frontend/subscription_plans.html')

def doctorAgreement(request):
    return render(request, 'frontend/doctorsAgreement.html')


def doctorBankDetails(request):
    return render(request, 'frontend/doctor_bank_details.html')

def doctorTimings(request):
    return render(request, 'frontend/doctorTimings.html')


def doctorBillPayments(request):
    return render(request, 'frontend/billPayments.html')

def prescription(request):
    return render(request, 'frontend/prescriptions.html')

def searchUI(request):
    return render(request, 'frontend/search.html',{"search_term":request.GET.get('term')})