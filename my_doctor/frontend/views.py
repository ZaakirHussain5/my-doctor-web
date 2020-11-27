from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from specialist_type.models import specialist_type
from patients.models import patient_info
from doctors.models import doctors_info
from consultations.models import consultations
from appointment.api import today_total_appointment
from doctor_payments.api import today_total_doctor_paid
from consultations.api import today_collected_commision

def login(request):
    user_type = ""
    if request.GET.get('user') == 'admin':
        user_type = "A"
    else:
        user_type = "E"
    return render(request,'auth/login.html', context = { "user_type":user_type})

def dashboard(request):
    context = {}
    today_doctor_paid = today_total_doctor_paid()
    print(today_doctor_paid)
    if today_doctor_paid['paid_amount__sum' ] is None:
        context['doctor_paid'] = 0.00
    else:
        context['doctor_paid'] = today_doctor_paid['paid_amount__sum']
    appointments_count_and_fees = today_total_appointment()
    print(appointments_count_and_fees['total_fees']['paid_amount__sum'])
    context['total_appointment'] = appointments_count_and_fees['total_count']
    context['fees'] = appointments_count_and_fees['total_fees']['paid_amount__sum']
    todays_commision = today_collected_commision()
    if todays_commision['comp_share__sum'] is None:
        context['commision'] = 0.00
    else:
        context['commision'] = todays_commision['comp_share__sum']
    return render(request,'auth/dashboard.html', context)

def specialists(request):
    return render(request,'frontend/specialists.html')

def Doctors(request):
    return render(request,'frontend/Doctors.html',{
        "specialist_types":specialist_type.objects.all()
    })

def DoctorsLists(request):
    return render(request, 'frontend/DoctorsLists.html', {
        "specialist_types":specialist_type.objects.all()
    })

    
def doctor_info(request, id):
    return render(request, 'frontend/doctorInfo.html', {'id': id})


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

def mis_reports(request):
    return render(request, 'frontend/mis_reports.html')

def appointments(request):
    return render(request, 'frontend/appointments.html')

def patients_details(request, id=None):
    return render(request, 'frontend/patientsInfo.html', {'id': id})

