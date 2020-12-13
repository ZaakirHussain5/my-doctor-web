import datetime 
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.mixins import UpdateModelMixin
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import date
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from my_doctor.settings import EMAIL_HOST_USER
from knox.models import AuthToken
from accounts.serializers import UserAuthSerializer
from specialist_type.models import specialist_type
from appointment.models import appointment
from .models import doctors_info, DoctorTimings, settlement_details, DoctorBankDetails, Doctornotes
from .serializers import *
from django.contrib.auth.models import User

class doctors_infoViewSet(viewsets.ModelViewSet):
    queryset = doctors_info.objects.filter(web_registration=False, is_active=True)
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = doctors_infoSerializer

    def perform_destroy(self, serializer):
        user_id = serializer.user.id
        u = User.objects.get(id=user_id)
        u.delete()
        return

class doctor_info_adminViewSet(viewsets.ModelViewSet):
    serializer_class = doctors_listSerializer
    permissions = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        id = self.request.query_params.get('id')
        return doctors_info.objects.filter(id= id)


class DoctorRegisterAPI(generics.GenericAPIView):
    serializer_class = DoctorRegistration

    def get_queryset(self):
        return doctors_info.objects.all()

    def send_mails(self, obj, password):
        mail_subject = 'Activate your account.'
        message = render_to_string('emails/doctorRegistrationEmail.html', {
            'full_name': obj.full_name,
            'username': obj.user.username,
            "password": password
        })

        msg = EmailMessage(
            'Subject',
            message,
            'Doctor Plus <'+ EMAIL_HOST_USER + '>',
            [obj.user.email],
        )
        msg.content_subtype = "html"  # Main content is now text/html
        try:
            msg.send()
        except:
            pass
        return True

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        self.send_mails(doctors_info.objects.get(user=user), request.data['password'])
        return Response({
            "Doctor": UserAuthSerializer(user, context=self.get_serializer_context()).data
        })


class DoctorTimingsAPI(viewsets.ModelViewSet):
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = DoctorTimingsSerializer

    def get_queryset(self):
        
        queryset = DoctorTimings.objects.filter(doctor__user=self.request.user)

        day = self.request.query_params.get('name')
        if day is not None :
            queryset = DoctorTimings.objects.filter(doctor__user=self.request.user, day=self.request.query_params.get('name'))
        return queryset   

    def perform_create(self, serializer):
        print(serializer)
        try:
            DoctorTimings.objects.get(doctor__user=self.request.user, day=serializer.validated_data['day']).delete()
        except ObjectDoesNotExist:
            pass
        doctor = doctors_info.objects.get(user = self.request.user)
        serializer.save(doctor=doctor)

    


class DoctorUpdateProfileAPI(generics.GenericAPIView, UpdateModelMixin):
    serializer_class = doctorUpdateProfileSerializer
    queryset = doctors_info.objects.all()
    lookup_field = 'id'
    permission_classes = [
        permissions.IsAuthenticated
    ]
    # lookup_field = 'id'
    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.save(loggedInuser=self.request.user.id)
    #     print(user)
    #     return Response({
    #         "Patient": UserAuthSerializer(user, context=self.get_serializer_context()).data,
    #         "token": AuthToken.objects.create(user)[1]
    #     })

    def put(self, request, *args, **kwargs):
        email = request.data.get('email', None)
        if email:
            user = request.user
            user.email = email
            user.save()
        return self.partial_update(request, *args, **kwargs)

class DoctorUpdateProfileAdminAPI(generics.GenericAPIView, ):
    serializer_class = UpdateProfile

    permission_classes = [
        permissions.AllowAny
    ]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        doctor_obj = doctors_info.objects.get(id=request.data['id'])
        user = serializer.save(loggedInuser=doctor_obj.user.id)
        print(user)
        return Response({
            "Patient": UserAuthSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class GetLoggedDoctor(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = doctors_listSerializer

    def get_object(self):
        try:
            doctor = doctors_info.objects.get(user__id=self.request.user.id)
            return doctor
        except ObjectDoesNotExist:
            return Response({
                "Message": "User Not Found"
            }, status=404)


class getAvailableDoctors(viewsets.ModelViewSet):
    serializer_class = AvlDoctorsListSerializer

    def get_queryset(self):
        day = self.request.query_params.get('day', None)
        spl = self.request.query_params.get('spl', None)
        queryset = doctors_info.objects.all()
        print(day, spl)
        if spl is not None:
            self.serializer_class = doctors_infoSerializer
            queryset = doctors_info.objects.filter(specialist_type=spl)
        if day is not None:
            if day == 'mon':
                queryset = DoctorTimings.objects.filter(
                    mon=True).filter(doctor__in=queryset)
            if day == 'tue':
                queryset = DoctorTimings.objects.filter(
                    tue=True).filter(doctor__in=queryset)
            if day == 'wed':
                queryset = DoctorTimings.objects.filter(
                    wed=True).filter(doctor__in=queryset)
            if day == 'thu':
                queryset = DoctorTimings.objects.filter(
                    thu=True).filter(doctor__in=queryset)
            if day == 'fri':
                queryset = DoctorTimings.objects.filter(
                    fri=True).filter(doctor__in=queryset)
            if day == 'sat':
                queryset = DoctorTimings.objects.filter(
                    sat=True).filter(doctor__in=queryset)
            if day == 'sun':
                queryset = DoctorTimings.objects.filter(
                    sun=True).filter(doctor__in=queryset)
        return queryset


class getAvailableDoctorsForApponment(viewsets.ModelViewSet):
    serializer_class = AvlDoctorsListSerializer

    def get_queryset(self):
        date = self.request.query_params.get('date')
        specialist_id = self.request.query_params.get('id')
        day, month, year = date.split('/')
        dates = datetime.date(int(year), int(month), int(day))
        day_name = dates.strftime("%A").lower()
        today_date = datetime.date.today()
        # if dates == today_date:
        #     print('matched')

        queryset = DoctorTimings.objects.filter(day = day_name, doctor__specialist_type = specialist_type.objects.get(id=specialist_id))
        for doctor in queryset:
            total_appiontments = appointment.objects.filter(doctor__id=doctor.doctor.id, appointment_date=date).count()
            if dates == today_date:
                current_datetime = datetime.datetime.now()
                str_make_date = str(year) + '-' + str(month) + '-' + str(day) + ' '+ doctor.to_time
                to_time = datetime.datetime.strptime(str_make_date, "%Y-%m-%d %H:%M")
                if current_datetime < to_time:
                    str_from_time = str(year) + '-' + str(month) + '-' + str(day) + ' ' + doctor.from_time
                    from_times = datetime.datetime.strptime(str_from_time, "%Y-%m-%d %H:%M")
                    if total_appiontments > 0:
                        # str_time = doctor.from_time
                        # date_format = datetime.datetime.strptime(str_time, '%H:%M')
                        # to_time = datetime.datetime.strptime(doctor.to_time, '%H:%M')
                        # from_times = date_format + datetime.timedelta( minutes= 10 * total_appiontments )
                        if (from_times < to_time):
                            if from_times < current_datetime:
                                # doctor.from_time = current_datetime + datetime.timedelta( minutes= 10 )
                                appointment_time = current_datetime + datetime.timedelta( minutes= 10 )
                        
                                doctor.from_time = datetime.datetime.strftime(appointment_time, '%H:%M')
                            
                            else:
                                doctor.from_time = datetime.datetime.strftime(from_times, '%H:%M')
                        else:
                            queryset = queryset.exclude(id= doctor.id)

                    else:
                        appointment_time = current_datetime + datetime.timedelta( minutes= 10 )
                        if appointment_time < to_time:
                            doctor.from_time = datetime.datetime.strftime(appointment_time, '%H:%M')
                        else:
                            queryset = queryset.exclude(id= doctor.id)
                else:
                    queryset = queryset.exclude(id= doctor.id)
                

            else:
                if total_appiontments > 0:
                    str_time = doctor.from_time
                    date_format = datetime.datetime.strptime(str_time, '%H:%M')
                    to_time = datetime.datetime.strptime(doctor.to_time, '%H:%M')
                    from_times = date_format + datetime.timedelta( minutes= 10 * total_appiontments )
                    if (from_times < to_time):
                        doctor.from_time = datetime.datetime.strftime(from_times, '%H:%M')
                    else:
                        queryset = queryset.exclude(id= doctor.id)


        return queryset



class DoctorLogout(generics.GenericAPIView):
    def post(self, request):
        if request.user is not None:
            doctor = doctors_info.objects.get(
                user=request.user)
            doctor.is_loggedin=False
            doctor.save()
            return Response({})


class NewDoctorRegistration(generics.GenericAPIView):
    serializer_class = WebNewDoctorRegistrationSerializer

    def send_mails(self, obj):
        mail_subject = 'Activate your account.'
        message = render_to_string('emails/doctorRegistrationEmail.html', {
            'username': obj.full_name,
            
        })

        msg = EmailMessage(
            'Subject',
            message,
            'Doctor Plus <'+ EMAIL_HOST_USER + '>',
            [obj.user.email],
        )
        msg.content_subtype = "html"  # Main content is now text/html
        try:
            msg.send()
        except:
            pass
        return True

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        self.send_mails(doctors_info.objects.get(user=user))
        return Response({
            "Doctor": UserAuthSerializer(user, context=self.get_serializer_context()).data
        })


class webdoctorViewset(viewsets.ModelViewSet):
    queryset = doctors_info.objects.filter(web_registration=True)
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = doctors_listSerializer


class get_settlement_details(viewsets.ModelViewSet):
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = settlement_detailsSerializer
    def get_queryset(self):
        doctor_id = self.request.query_params.get('id')
        return  settlement_details.objects.filter(doctor_id__id = doctor_id)

    # def perform_create(self, serializer):
    #     details = settlement_details.objects.get(doctor_id__id=self.request.data['doctor_id'])


class specificDoctorSettlement(viewsets.ModelViewSet):

    permissions = [
        permissions.AllowAny
    ]
    serializer_class = settlement_detailsSerializer

    def get_queryset(self):
        id = self.request.query_params.get('doctor_id')
        print("id is ", id)
        doctor = doctors_info.objects.get(Registration_Number=id)
        return settlement_details.objects.filter(doctor_id=doctor)


class get_doctor_bankDetails(viewsets.ModelViewSet):
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = DoctorBankDetailsSerializer
    queryset = DoctorBankDetails.objects.all()


class doctor_agreement_list(viewsets.ModelViewSet):
    serializer_class = doctors_listSerializer
    permissions = [
        permissions.AllowAny
    ]

    queryset = doctors_info.objects.filter(is_active=True)


class doctorRegistrationAdmin(generics.GenericAPIView):
    serializer_class = UpdateProfile

    permission_classes = [
        permissions.AllowAny
    ]

    def send_mails(self, obj):
        mail_subject = 'Activate your account.'
        message = render_to_string('emails/pendingDoctorAcception.html', {
            'full_name': obj.full_name,
            'username': obj.user.username
        })

        msg = EmailMessage(
            'Subject',
            message,
            'Doctor Plus <'+ EMAIL_HOST_USER + '>',
            [obj.user.email],
        )
        msg.content_subtype = "html"  # Main content is now text/html
        try:
            msg.send()
        except:
            pass
        return True


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        input_username = request.data['username']
        user = User.objects.get(username=input_username)
        user = serializer.save(loggedInuser=user.id)
        print(user)
        self.send_mails(doctors_info.objects.get(user=user))
        return Response({
            "Doctor": UserAuthSerializer(user, context=self.get_serializer_context()).data,
        })


class DoctorTimingsAdminAPI(viewsets.ModelViewSet):
    permissions = [
        permissions.IsAuthenticated
    ]
    serializer_class = DoctorTimingsSerializer

    def get_queryset(self):
        id = self.request.GET.get('id')
        return DoctorTimings.objects.filter(doctor_id=id)

    def perform_create(self, serializer):
        try:
            timing_id = self.request.data['id']
            print("timing_id=====", timing_id)
            if timing_id != '':
                old_timing = DoctorTimings.objects.get(id=timing_id)
                old_timing.delete()
        except ObjectDoesNotExist:
            pass
        serializer.save()

class DoctorTimingsApiView(viewsets.ModelViewSet):
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = DoctorTimingsSerializer

    def get_queryset(self):
        
        doctor_id = self.request.query_params.get('id', None)
        if doctor_id:
            doctor = doctors_info.objects.get(id=doctor_id)
            queryset = DoctorTimings.objects.filter(doctor=doctor)
        day = self.request.query_params.get('name')
        if day is not None :
            queryset = DoctorTimings.objects.filter(doctor=doctor, day=self.request.query_params.get('name'))
        return queryset 

    def perform_create(self, serializer):
        print(serializer)
        doctor = doctors_info.objects.get(id = self.request.data['doctor_id'])

        try:
            DoctorTimings.objects.get(doctor=doctor, day=serializer.validated_data['day']).delete()
        except ObjectDoesNotExist:
            pass
        serializer.save(doctor=doctor)

    def destroy(self, request, pk=None):
        if pk is not None:
            doctor_timings = DoctorTimings.objects.get(id=pk)
            doctor_timings.delete()
            return Response({'ok': 'ok'})
    


class changeFee(APIView):
    def post(self, request, format=None):
        doctor = doctors_info.objects.get(user=request.user)
        doctor.consultation_fee = request.data['new_fees']
        doctor.save()
        print(doctor)
        serializer = doctors_listSerializer(doctor)
        return Response(serializer.data)


class changeFeeByAdmin(APIView):
    def post(self, request, format=None):
        doctor_id = request.POST.get('doctor_id')
        doctor = doctors_info.objects.get(id=doctor_id)
        doctor.consultation_fee = request.data['new_fees']
        doctor.save()
        print(doctor)
        serializer = doctors_listSerializer(doctor)
        return Response(serializer.data)


class doctor_bankDetails(viewsets.ModelViewSet):
    permissions = [
        permissions.IsAuthenticated
    ]
    serializer_class = DoctorsBankDetailsSerializer

    def get_queryset(self):
        return DoctorBankDetails.objects.filter(doctor_id=doctors_info.objects.get(user=self.request.user))

    def perform_create(self, serializer):
        serializer.save(doctor_id=doctors_info.objects.get(
            user=self.request.user))


class doctor_bankDetailsAdminView(viewsets.ModelViewSet):
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = DoctorsBankDetailsSerializer

    def get_queryset(self):
        doctor_id = self.request.query_params.get('id')
        return DoctorBankDetails.objects.filter(doctor_id=doctors_info.objects.get(id=doctor_id))

    def perform_create(self, serializer):
        doctor_ids = self.request.data.get('doctor_id')
        print(doctor_ids)
        try:
            DoctorBankDetails.objects.get(doctor_id=doctors_info.objects.get(id=doctor_ids)).delete()
        except:
            pass

        serializer.save(doctor_id=doctors_info.objects.get(
            id=doctor_ids))



class doctor_notesView(viewsets.ModelViewSet):
    serializer_class = DoctornotesSerializer
    permissions = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        doctor_id = self.request.query_params.get('id')
        return Doctornotes.objects.filter(doctor=doctors_info.objects.get(id=doctor_id))

    def perform_create(self, serializer):
        doctor_is = self.request.data.get('doctor_id')
        doctor_info = doctors_info.objects.get(id=doctor_is)
        try: 
            Doctornotes.objects.get(doctor=doctor_info).delete()
        except:
            pass

        serializer.save(doctor = doctor_info)



class specific_doctor_available(viewsets.ModelViewSet):
    serializer_class = AvlDoctorsListSerializer 

    def get_queryset(self):
        date = self.request.query_params.get('date')
        doctor_id = self.request.query_params.get('id')
        doctors = appointment.objects.get(id=doctor_id)
        print(date)
        day, month, year = date.split('/')
        print(int(year), int(month), int(day))
        day_name = datetime.date(int(year), int(month), int(day))
        day_name = day_name.strftime("%A").lower()
        queryset = DoctorTimings.objects.filter(day = day_name, doctor=doctors.doctor)
        for doctor in queryset:
            total_appiontments = appointment.objects.filter(doctor__id=doctor.doctor.id, appointment_date=date).count()
            if total_appiontments > 0:
                str_time = doctor.from_time
                date_format = datetime.datetime.strptime(str_time, '%H:%M')
                to_time = datetime.datetime.strptime(doctor.to_time, '%H:%M')
                from_times = date_format + datetime.timedelta( minutes= 10 * total_appiontments )
                if (from_times < to_time):
                    doctor.from_time = datetime.datetime.strftime(from_times, '%H:%M')
                else:
                    queryset = queryset.exclude(id= doctor.id)
        return queryset       

class check_phone_no(generics.GenericAPIView):
    def post(self, request):
        phone_no = request.data['ph_no']
        all_doctors = doctors_info.objects.filter(phone_number=phone_no)
        if len(all_doctors) == 1:
            return Response({
                'doctor_available': True,
                'doctor': doctors_infoSerializer(all_doctors[0]).data
            })

        else:
            return Response({
                'doctor_available': False
            })

class change_password(generics.GenericAPIView):
    def post(self, request):
        pat_id = request.data['id']
        patient = doctors_info.objects.get(id=pat_id)
        user = patient.user
        user.set_password(request.data['password'])
        user.save()
        return Response({
            'password_change': True
        })