from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,  redirect
from django.urls import reverse
from specialist_type.models import specialist_type
from patients.models import patient_info
from doctors.models import doctors_info
from consultations.models import consultations
from appointment.api import today_total_appointment
from doctor_payments.api import today_total_doctor_paid
from consultations.api import today_collected_commision
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.db.models import Count


from lab_tests.models import lab_tests, lab_tests_parameters_type, lab_tests_parameter, lab_tests_faqs, lab_tests_purchase


def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']  
        password = request.POST['password'] 
        user = authenticate(request, username = username, password=password)
        if user:
            login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            return redirect('/admin/')

    return render(request,'auth/login.html')

@login_required(login_url='/adminlogin')
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
    context['fees'] = 0.00
    if appointments_count_and_fees['total_fees']['paid_amount__sum']:
        context['fees'] = appointments_count_and_fees['total_fees']['paid_amount__sum']
        
    todays_commision = today_collected_commision()
    if todays_commision['comp_share__sum'] is None:
        context['commision'] = 0.00
    else:
        context['commision'] = todays_commision['comp_share__sum']
    return render(request,'auth/dashboard.html', context)

@login_required(login_url='/adminlogin')
def specialists(request):
    return render(request,'frontend/specialists.html')

@login_required(login_url='/adminlogin')
def Doctors(request):
    return render(request,'frontend/Doctors.html',{
        "specialist_types":specialist_type.objects.all()
    })

@login_required(login_url='/adminlogin')
def DoctorsLists(request):
    return render(request, 'frontend/DoctorsLists.html', {
        "specialist_types":specialist_type.objects.all()
    })

@login_required(login_url='/adminlogin')
def doctor_info(request, id):
    return render(request, 'frontend/doctorInfo.html', {'id': id})

@login_required(login_url='/adminlogin')
def Executives(request):
    return render(request,'frontend/Executives.html')

@login_required(login_url='/adminlogin')
def customerCareDashboard(request):
    return render(request,'frontend/customerCareDashboard.html')

@login_required(login_url='/adminlogin')
def patientsList(request):
    return render(request,'frontend/patientsList.html')


@login_required(login_url='/adminlogin')
def newAppointment(request):
    context = {}
    patient_id = request.GET.get('patient')
    print(patient_id)
    patient_data = patient_info.objects.get(id=patient_id)
    print(patient_data)
    context['patient_info'] = patient_data
    return render(request,'frontend/newAppointment.html', context)

@login_required(login_url='/adminlogin')
def consultationsList(request):
    return render(request, 'frontend/consultationsList.html')


@login_required(login_url='/adminlogin')
def webDoctorList(request):
    return render(request, 'frontend/doctorsList.html')

@login_required(login_url='/adminlogin')
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


@login_required(login_url='/adminlogin')
def viewDoctorPayment(request):
    return render(request, 'frontend/doctorPaymentsList.html')


@login_required(login_url='/adminlogin')
def reminders(request):
    return render(request,'frontend/reminders.html')

@login_required(login_url='/adminlogin')
def EnquiresList(request):
    return render(request, 'frontend/enquiresList.html')


@login_required(login_url='/adminlogin')
def labtests(request):
    return render(request, 'frontend/labtests.html')


@login_required(login_url='/adminlogin')
def doctorAgreement(request):
    return render(request, 'frontend/doctorsAgreement.html')

@login_required(login_url='/adminlogin')
def doctorBankDetails(request):
    return render(request, 'frontend/doctor_bank_details.html')


@login_required(login_url='/adminlogin')
def doctorTimings(request):
    return render(request, 'frontend/doctorTimings.html')

@login_required(login_url='/adminlogin')
def doctorBillPayments(request):
    return render(request, 'frontend/billPayments.html')


@login_required(login_url='/adminlogin')
def prescription(request):
    return render(request, 'frontend/prescriptions.html')


@login_required(login_url='/adminlogin')
def searchUI(request):
    return render(request, 'frontend/search.html',{"search_term":request.GET.get('term')})


@login_required(login_url='/adminlogin')
def mis_reports(request):
    if request.user.is_superuser:
        return render(request, 'frontend/mis_reports.html')
    return HttpResponseRedirect(reverse('adminDashboard'))


@login_required(login_url='/adminlogin')
def appointments(request):
    return render(request, 'frontend/appointments.html')


@login_required(login_url='/adminlogin')
def patients_details(request, id=None):
    return render(request, 'frontend/patientsInfo.html', {'id': id})


@login_required(login_url='/adminlogin')
def promo_code(request):
    return render(request, 'frontend/promo_code.html')

@login_required(login_url='/adminlogin')
def lab_Tests_packages(request):
    context = {}
    context['labtest'] = lab_tests.objects.get(id=request.GET.get('id'))
    context['lab_test_parameter_type'] = lab_tests_parameters_type.objects.all()
    context['parametes'] = lab_tests_parameter.objects.all()
    context['faqs'] = lab_tests_faqs.objects.filter(lab_test__id=request.GET.get('id')).order_by('-id')
    return render(request, 'frontend/manage_lab_test.html', context)


@login_required(login_url='/adminlogin')
def loutoutView(request):
    logout(request)
    return redirect('/adminlogin')


@login_required(login_url='/adminlogin')
def labTest_perches(request):
    return render(request, 'frontend/labtest_perches.html') 


@login_required(login_url='/adminlogin')
def purches_files(request, id):
    context={}
    lab_test_file = lab_tests_purchase.objects.get(id=id)
    lab_test_type = lab_tests_parameters_type.objects.filter(lab_test=lab_test_file.lab_test_id)
    lab_test_types = lab_test_type.annotate(total = Count('type_children'))
    context['lab_test_types'] = lab_test_types
    totalParameter = 0
    for types in lab_test_types:
        totalParameter += types.total
    context['total_parameters'] = totalParameter
    context['parameters'] = lab_tests_parameter.objects.filter(parameter_type__in=lab_test_type)
    
    context["lab_file"] = lab_test_file
    return render(request, 'frontend/labTestFile.html', context)














