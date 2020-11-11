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

def newAppointment(request):
    context ={}
    context['specialist']=specialist_type.objects.all()
    return render(request,'patientsUI/new_appointment.html', context)

def billHistory(request):
    return render(request,'patientsUI/bill_history.html')

def medical_records(request):
    return render(request,'patientsUI/medical_records.html')

def plan(request):
    return render(request,'patientsUI/plan.html')