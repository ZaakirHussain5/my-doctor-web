from django.shortcuts import render,redirect
from specialist_type.models import specialist_type
from consultations.models import consultations as consultationTable
from patient_subscription.models import PatientSubscription
from patients.models import patient_info
from django.contrib.auth.decorators import login_required
from patient_subscription.models import PatientSubscription


@login_required(login_url='/login')
def dashboard(request):
    return render(request,'patientsUI/dashboard.html')

@login_required(login_url='/login')
def old_dashboard(request):
    return render(request,'patientsUI/old_dashboard.html')

@login_required(login_url='/login')
def appointments(request):
    return render(request,'patientsUI/appointments.html')

@login_required(login_url='/login')
def consultations(request):
    return render(request,'patientsUI/consultations.html')

@login_required(login_url='/login')
def selectDoctors(request):
    spl_type = specialist_type.objects.get(special_type=request.GET.get('spl'))
    print(spl_type)
    reqDate=request.GET.get('date').split('/')
    weekDays={0:"mon",1:"tue",2:"wed",3:"thu",4:"fri",5:"sat",6:"sun"}
    import datetime
    week = datetime.datetime(int(reqDate[2]),int(reqDate[1]),int(reqDate[0])).weekday()
    return render(request,'patientsUI/selectDoctors.html',{
        "specialist":spl_type,
        "date":request.GET.get('date'),
        "week":weekDays[week]
    })

@login_required(login_url='/login')
def newAppointment(request):
    try:
        patient = patient_info.objects.get(user=request.user)
    except:
        return redirect('/login')
    context ={}
    context['specialist']=specialist_type.objects.all()
    context["subscription_active"] = 'no'
    try:
        pat_sub = PatientSubscription.objects.get(user=patient, is_active=True)
        context["subscription_active"] = 'yes'
    except PatientSubscription.DoesNotExist:
        context["subscription_active"] = 'no'
    return render(request,'patientsUI/new_appointment.html', context)

@login_required(login_url='/login')
def billHistory(request):
    return render(request,'patientsUI/bill_history.html')

@login_required(login_url='/login')
def medical_records(request):
    return render(request,'patientsUI/medical_records.html')

@login_required(login_url='/login')
def plan(request):
    try:
        patient = patient_info.objects.get(user=request.user)
    except:
        return redirect('/login')
    context = {}
    print('age is ', patient.age)
    if patient.age == None or patient.age == '':
        context['is_senior'] = 'nodata'
    else:
        if int(patient.get_age) >= 65:
            context['is_senior'] = 'eligable'
        else:
            context['is_senior'] = 'noteligable'
    print(context)
    try:
        pat_sub = PatientSubscription.objects.get(user=patient, is_active=True)
        context['active_plan'] = pat_sub
        context["planExists"] = True
    except PatientSubscription.DoesNotExist:
        context["planExists"] = False
    return render(request,'patientsUI/plan.html',context)


@login_required(login_url='/login')
def invoice(request):
    const_id = request.GET.get('id', None)
    consultationInstance = consultationTable.objects.get(id=const_id)
    context = {
        "consultation" : consultationInstance 
    }
    context['tax']= (consultationInstance.comp_share * 18) / 100
    return render(request,'patientsUI/invoice.html', context)



def patientInvoice(request):
    context = {}
    pat_subs_id = request.GET.get('id', None)
    try:
        subscriptionData = PatientSubscription.objects.get(id=pat_subs_id)
        context['plan'] = subscriptionData
    except PatientSubscription.DoesNotExist:
        pass
    print(context)
    return render(request,'patientsUI/subscriptionInvoice.html', context)