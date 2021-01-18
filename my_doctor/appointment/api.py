import asyncio
from .serializers import appointmentSerializer,appointmentsListSerializer, cancleAppointmentSerializer
from .models import appointment
from rest_framework import viewsets, permissions,mixins
from datetime import date, datetime
from django.db.models import Sum
from transactions.models import transactions
from patients.models import patient_info
from promo_codes.models import promo_code, AppliedPromoCode
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from my_doctor.settings import EMAIL_HOST_USER
import requests
import json

url = "https://teleduce.corefactors.in/send-email-json-otom/a224db72-cafb-4cce-93ab-3d7f950c92e2/1009/"


def today_total_appointment():
    date = getDateFormat()
    print(date)
    appointments = appointment.objects.filter(appointment_date= date)
    total_fees_collected = appointments.aggregate(Sum('paid_amount'))
    obj = {
        'total_count': appointments.count(),
        'total_fees': total_fees_collected
    }
    return obj


def get_a_range_appointment(from_date, to_date):
    total_appointmetns = appointment.objects.filter(created_at__date__range=(from_date, to_date))
    total_fees_collected = total_appointmetns.aggregate(Sum('paid_amount'))
    obj = {
        'total_count': total_appointmetns.count(),
        'total_fees': total_fees_collected
    }
    return obj 

def getDateFormat():
    d = date.today()
    year = '{:02d}'.format(d.year)
    month = '{:02d}'.format(d.month)
    day = '{:02d}'.format(d.day)
    formated_date = '{0}/{1}/{2}'.format(day, month, year)

    return formated_date

class appointmentViewSet(viewsets.ModelViewSet):
    permissions = [
        permissions.IsAuthenticated
    ]
    serializer_class = appointmentSerializer

    def send_mails(self, obj):
        url = "https://teleduce.corefactors.in/send-email-json-otom/a224db72-cafb-4cce-93ab-3d7f950c92e2/1009/"
        patient = patient_info.objects.get(user= obj.patient)
        messages = render_to_string('emails/newAppointmentspatient.html', {
            'full_name': patient.full_name,
            'doctor': obj.doctor.full_name,
            "date": obj.appointment_date,
            "time": obj.appointment_time,
            'patient': patient.full_name
        })
        to_list=[{"email_id":patient.user.email,"name":patient.full_name}]
        message = {
        "html_content": messages,
        "subject":"New Appointment",
        "from_mail":"bstejas@doctor-plus.in",
        "from_name":"doctor Plus",
        "to_recipients":to_list,
        "reply_to": "bstejas@doctor-plus.in"
        }
        payload = {"message" :message}
        single_content = {"mail_datas":payload}
        reqdata = requests.post(url, data=json.dumps(single_content))
        
        Doctor_message = render_to_string('emails/newAppointmentDoctor.html', {
            'full_name': obj.doctor.full_name,
            "date": obj.appointment_date,
            "time": obj.appointment_time,
            'patient': patient.full_name
        })
        to_list=[{"email_id":obj.doctor.user.email,"name":obj.doctor.full_name}]
        message = {
        "html_content": messages,
        "subject":"New Appointment",
        "from_mail":"bstejas@doctor-plus.in",
        "from_name":"doctor Plus",
        "reply_to": "bstejas@doctor-plus.in",
        "to_recipients":to_list
        }
        payload = {"message" :message}
        single_content = {"mail_datas":payload}
        reqdata = requests.post(url, data=json.dumps(single_content))
        
        return True

    def get_queryset(self):
        return self.request.user.appointments.all()

    def perform_create(self, serializer):
        promocodes = self.request.data.get('promocode', None)
        print('dvsv =====>>s', promocodes)
        if promocodes is not None:
            
            promoCode = promo_code.objects.get(code=promocodes)
            print('promo code ', promoCode)
            used_promo = AppliedPromoCode(code=promocodes, patient=self.request.user)
            used_promo.save()
            # except promo_code.DoesNotExist:
            #     pass
        new_appointmets = serializer.save(patient=self.request.user)
        self.send_mails(new_appointmets)


    def perform_update(delf, serializer):
        if serializer.is_valid(raise_exception=False):
            serializer.save()
        return 



class NewAppointmentAPI(viewsets.ModelViewSet):
    queryset = appointment.objects.all()
    serializer_class = appointmentSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class getPatientAppointments(mixins.ListModelMixin, viewsets.GenericViewSet):
    
    permissions = [
        permissions.IsAuthenticated
    ]
    serializer_class = appointmentsListSerializer
   
    def get_queryset(self):
        return self.request.user.appointments.all()

class getAppoinmentHistory(viewsets.ModelViewSet):
    serializer_class = appointmentsListSerializer
    permission = (
        permissions.IsAuthenticated
    )
    def get_queryset(self):
        return appointment.objects.filter(patient = self.request.user).exclude(consultation_status='Pending')

class getUpcomingAppoinment(viewsets.ModelViewSet):
    serializer_class = appointmentsListSerializer
    permission = (
        permissions.IsAuthenticated
    )

    def get_queryset(self):
        return appointment.objects.filter(consultation_status = 'Pending', patient=self.request.user).order_by('created_at')


class upComingAppoinment(viewsets.ModelViewSet):
    serializer_class = appointmentsListSerializer
    permission = (
        permissions.IsAuthenticated
    )

    def get_queryset(self):
        dates = getDateFormat()
        return appointment.objects.filter(consultation_status = 'Pending', doctor__user=self.request.user).exclude(appointment_date__contains=dates).order_by('created_at')


class previousAppoinment(viewsets.ModelViewSet):
    serializer_class = appointmentsListSerializer
    permission = (
        permissions.IsAuthenticated
    )

    def get_queryset(self):
        return appointment.objects.filter(consultation_status = 'Completed', doctor__user=self.request.user)


class todaysAppoinment(viewsets.ModelViewSet):
    serializer_class = appointmentsListSerializer
    permission = (
        permissions.IsAuthenticated
    )

    def get_queryset(self):
        formated_date = getDateFormat()
        print(formated_date)
        return appointment.objects.filter(consultation_status = 'Pending', appointment_date__contains=formated_date,  doctor__user=self.request.user).order_by('created_at')



class getDoctorAppointments(mixins.ListModelMixin, viewsets.GenericViewSet):
    
    permissions = [
        permissions.IsAuthenticated
    ]
    serializer_class = appointmentsListSerializer
   
    def get_queryset(self):
        return appointment.objects.filter(doctor__user=self.request.user)



class getAllAppointments(mixins.ListModelMixin, viewsets.GenericViewSet):
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = appointmentsListSerializer

    def get_queryset(self):
        queryset = appointment.objects.all()
        status = self.request.query_params.get('status',None)
        now = self.request.query_params.get('now',None)
        formated_date = getDateFormat()
        print(status)
        if status is not None:
            if status == 'Completed':
                queryset =  appointment.objects.filter(consultation_status__icontains=status)
            else:
                queryset =  appointment.objects.filter(consultation_status__icontains=status).exclude(appointment_date=formated_date)
        if now is not None:
            queryset =  appointment.objects.filter(consultation_status=status,appointment_date=formated_date)
        return queryset



class cancleAppointment(viewsets.ModelViewSet):
    serializer_class = cancleAppointmentSerializer
    queryset = appointment.objects.all()
    permissions = {
        permissions.IsAuthenticated
    }
    def perform_update(self, serializer):
        appointments = serializer.save()
        if appointments.consultation_status == 'Cancelled':
            now = datetime.now()
            desc = "Appointment Cancelled on {0}".format(now.strftime("%m/%d/%Y"))
            print(desc)
            trans = transactions(trans_type="Appointment Cancelled", trans_desc=desc,user_id = self.request.user, credit=appointments.paid_amount)
            trans.save()
            print(trans)

        return 


class getAllAppointmentsSpecificUser(viewsets.ModelViewSet):
    serializer_class = appointmentsListSerializer

    permissions = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        pat_id = self.request.query_params.get('pat_id')
        return appointment.objects.filter(patient=patient_info.objects.get(id=pat_id).user)
        
