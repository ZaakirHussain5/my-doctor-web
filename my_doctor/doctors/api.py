from .serializers import *
from .models import doctors_info, DoctorTimings, settlement_details, DoctorBankDetails
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from accounts.serializers import UserAuthSerializer
from django.core.exceptions import ObjectDoesNotExist
from knox.models import AuthToken
from datetime import date
from specialist_type.models import specialist_type
import datetime 
from rest_framework.views import APIView

class doctors_infoViewSet(viewsets.ModelViewSet):
    queryset = doctors_info.objects.filter(web_registration=False)
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = doctors_infoSerializer


class DoctorRegisterAPI(generics.GenericAPIView):
    serializer_class = DoctorRegistration

    def get_queryset(self):
        return doctors_info.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "Doctor": UserAuthSerializer(user, context=self.get_serializer_context()).data
        })


class DoctorTimingsAPI(viewsets.ModelViewSet):
    permissions = [
        permissions.IsAuthenticated
    ]
    serializer_class = DoctorTimingsSerializer

    def get_queryset(self):
        return DoctorTimings.objects.filter(doctor__user=self.request.user, day=self.request.query_params.get('name'))

    def perform_create(self, serializer):
        print(serializer)
        try:
            DoctorTimings.objects.get(doctor__user=self.request.user, day=serializer.validated_data['day']).delete()
        except ObjectDoesNotExist:
            pass
        doctor = doctors_info.objects.get(user = self.request.user)
        serializer.save(doctor=doctor)


class DoctorUpdateProfileAPI(generics.GenericAPIView):
    serializer_class = UpdateProfile

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save(loggedInuser=self.request.user.id)
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
        print(month, day, year)
        day_name = datetime.date(int(year), int(month), int(day))
        day_name = day_name.strftime("%A").lower()
        print(day_name)
        queryset = DoctorTimings.objects.filter(day = day_name, doctor__specialist_type = specialist_type.objects.get(id=specialist_id))
        return queryset



class DoctorLogout(generics.GenericAPIView):
    def post(self, request):
        if request.user is not None:
            doctor = doctors_info.objects.get(
                user=request.user).update(is_loggedin=False)
            doctor.save()
            return Response({})


class NewDoctorRegistration(generics.GenericAPIView):
    serializer_class = WebNewDoctorRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
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
    queryset = settlement_details.objects.all()


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

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        input_username = request.data['username']
        user = User.objects.get(username=input_username)
        user = serializer.save(loggedInuser=user.id)
        print(user)
        return Response({
            "Doctor": UserAuthSerializer(user, context=self.get_serializer_context()).data,
        })


class DoctorTimingsAdminAPI(viewsets.ModelViewSet):
    permissions = [
        permissions.AllowAny
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



class changeFee(APIView):
    def post(self, request, format=None):
        doctor = doctors_info.objects.get(user=request.user)
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
