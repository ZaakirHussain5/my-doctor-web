import asyncio
import requests
import json
from django.contrib.auth import logout
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import ( 
    UpdatePasswordSerializer, UpdateProfile,patient_infoSerializer,
    PatientResgistrationSerializer,medical_historySerializer,
    groupsSerializer,PatientResgistrationApp, UserEmail,
    PatientBillingHistorySerializer,patient_family_membersSerializer,
    socailRegistrationSerializer
)
from .models import (patient_info,medical_history,groups, PatientBillingHistory,patient_family_members)
from rest_framework import viewsets, permissions,generics
from rest_framework.response import Response
from accounts.serializers import UserAuthSerializer
from django.core.exceptions import ObjectDoesNotExist
from knox.models import AuthToken
from django.contrib.auth.models import User
from django.contrib.auth import login
from appointment.models import appointment
from appointment.serializers import appointmentSerializer
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from my_doctor.settings import EMAIL_HOST_USER
from django.contrib.auth import logout
from knox.models import AuthToken

class patient_infoViewSet(viewsets.ModelViewSet):
    queryset = patient_info.objects.filter(is_active=True)
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = patient_infoSerializer

    def perform_destroy(self, serializer):
        user_id = serializer.user.id
        u = User.objects.get(id=user_id)
        u.delete()
        return

class patient_family_membersViewset(viewsets.ModelViewSet):
    serializer_class = patient_family_membersSerializer
    permission_classes=[
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        return patient_family_members.objects.filter(patient__user=self.request.user)

    def perform_create(self,serializer):
        patient = patient_info.objects.get(user=self.request.user)
        serializer.save(patient=patient)
        



class SpecificPatient_infoViewSet(viewsets.ModelViewSet):
    
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = patient_infoSerializer

    def get_queryset(self):
        pat_id = self.request.query_params.get('pat_id')
        return patient_info.objects.filter(id = pat_id)



class PatientResgistrationAPI(generics.GenericAPIView):
    serializer_class = PatientResgistrationSerializer
    
    def get_queryset(self):
        return patient_info.objects.all()
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        pat_info = patient_info.objects.get(user=user)
        self.send_mails(pat_info, request.data['password'])
        return Response({
            "Patient": UserAuthSerializer(user, context=self.get_serializer_context()).data
        })

    
    def send_mails(self, obj, password):
        mail_subject = 'Activate your account.'
        messages = render_to_string('email.html', {
            'username': obj.full_name,
            'patient_id': obj.pat_id,
            'password': password
        })
        url = "https://teleduce.corefactors.in/send-email-json-otom/a224db72-cafb-4cce-93ab-3d7f950c92e2/1009/"
        
        to_list=[{"email_id":obj.user.email,"name":obj.full_name}]
        message = {
        "html_content": messages,
        "subject":mail_subject,
        "from_mail":"bstejas@doctor-plus.in",
        "from_name":"doctor Plus",
        "to_recipients":to_list,
        "reply_to": "bstejas@doctor-plus.in"
        }
        payload = {"message" :message}
        single_content = {"mail_datas":payload}
        reqdata = requests.post(url, data=json.dumps(single_content))
        return True






class PatientResgistrationAppAPI(generics.GenericAPIView):
    serializer_class = PatientResgistrationApp
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        pat = patient_info.objects.get(user=user)
        login(request,user)
        self.send_mails(pat, request.data['password'])
        return Response({
            "Patient": UserAuthSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

    def send_mails(self, obj, password):
        mail_subject = 'Activate your account.'
        messages = render_to_string('email.html', {
            'username': obj.full_name,
            'patient_id': obj.pat_id,
            'password': password
        })

        url = "https://teleduce.corefactors.in/send-email-json-otom/a224db72-cafb-4cce-93ab-3d7f950c92e2/1009/"
        
        to_list=[{"email_id":obj.user.email,"name":obj.full_name}]
        message = {
        "html_content": messages,
        "subject":mail_subject,
        "from_mail":"bstejas@doctor-plus.in",
        "from_name":"doctor Plus",
        "to_recipients":to_list,
        "reply_to": "bstejas@doctor-plus.in"
        }
        payload = {"message" :message}
        single_content = {"mail_datas":payload}
        reqdata = requests.post(url, data=json.dumps(single_content))

        return True


class socialPatientRegistrationView(generics.GenericAPIView):
    serializer_class = socailRegistrationSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        login(request,user)
        return Response({
            'Patient': UserAuthSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })



class PatientUpdateProfileAPI(generics.GenericAPIView):
    serializer_class = UpdateProfile

    permission_classes=[
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

class GetLoggedPatient(generics.RetrieveAPIView):
  permission_classes = [
    permissions.IsAuthenticated,
  ]
  serializer_class = patient_infoSerializer

  def get_object(self):
        try:
            patient = patient_info.objects.get(user__id=self.request.user.id)
            return patient
        except ObjectDoesNotExist:
            return Response({
                "Message":"User Not Found"
            },status=404)

class medical_historyViewSet(viewsets.ModelViewSet):
    queryset = medical_history.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = medical_historySerializer

class groupsViewSet(viewsets.ModelViewSet):
    queryset = groups.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = groupsSerializer


class PatientEmail(generics.RetrieveAPIView):
    permission_classes = [
    permissions.IsAuthenticated,
      ]
    serializer_class = UserEmail

    def get_object(self):
        try:
            patient = User.objects.get(id=self.request.user.id)
            return patient
        except ObjectDoesNotExist:
            return Response({
                "Message":"User Not Found"
            },status=404)

    
class PasswordChange(generics.GenericAPIView):
    permission_classes = [
    permissions.IsAuthenticated,
      ]
    serializer_class = UpdatePasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save(loggedInuser=self.request.user.id)
        print(user)
        return JsonResponse({'done': 'done'}, safe=False)


class PatientBillingHistorys(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PatientBillingHistorySerializer

    def get_queryset(self):
        queryset = PatientBillingHistory.objects.filter(patient__user = self.request.user).order_by('-date')
        #queryset = PatientBillingHistory.objects.all()
        return queryset

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return serializer


@api_view(['GET'])
def patientData(request):
    pat_id = request.query_params.get('id')
    print(pat_id)
    patient = patient_info.objects.get(id=id)
    appointment = appointment.objects.filter(patient=patient)
    data = {
        "pat_details": patient_infoSerializer(patient).data,
        "appoinmentHistory": appointmentSerializer(appointment)
    }

    return HttpResponse(data)

class PatientLogout(generics.GenericAPIView):
    def post(self, request):
        if request.user is not None:
            patient = patient_info.objects.get(
                user=request.user)
            patient.is_logged_in=False
            AuthToken.objects.filter(user=request.user).delete()
            patient.save()
            logout(request)
            return Response({})



class check_phone_no(generics.GenericAPIView):
    def post(self, request):
        phone_no = request.data['ph_no']
        all_patients = patient_info.objects.filter(ph_no=phone_no)
        if len(all_patients) == 1:
            return Response({
                'patient_available': True,
                'patient': patient_infoSerializer(all_patients[0]).data
            })

        else:
            return Response({
                'patient_available': False
            })


class cheange_password(generics.GenericAPIView):
    def post(self, request):
        pat_id = request.data['id']
        patient = patient_info.objects.get(id=pat_id)
        user = patient.user
        user.set_password(request.data['password'])
        user.save()
        return Response({
            'password_change': True
        })
