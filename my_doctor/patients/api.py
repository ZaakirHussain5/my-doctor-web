from django.contrib.auth import logout
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import ( 
    UpdatePasswordSerializer, UpdateProfile,patient_infoSerializer,
    PatientResgistrationSerializer,medical_historySerializer,
    groupsSerializer,PatientResgistrationApp, UserEmail,
    PatientBillingHistorySerializer,patient_family_membersSerializer
)
from .models import (patient_info,medical_history,groups, PatientBillingHistory,patient_family_members)
from rest_framework import viewsets, permissions,generics
from rest_framework.response import Response
from accounts.serializers import UserAuthSerializer
from django.core.exceptions import ObjectDoesNotExist
from knox.models import AuthToken
from django.contrib.auth.models import User
from appointment.models import appointment
from appointment.serializers import appointmentSerializer

class patient_infoViewSet(viewsets.ModelViewSet):
    queryset = patient_info.objects.filter(is_active=True)
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = patient_infoSerializer

    def perform_destroy(self, serializer):
        serializer.is_active = False
        serializer.save()
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
        return Response({
            "Patient": UserAuthSerializer(user, context=self.get_serializer_context()).data
        })

class PatientResgistrationAppAPI(generics.GenericAPIView):
    serializer_class = PatientResgistrationApp
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "Patient": UserAuthSerializer(user, context=self.get_serializer_context()).data,
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
        # queryset = PatientBillingHistory.objects.filter(patient = patient_info.objects.get(user = self.request.user))
        queryset = PatientBillingHistory.objects.all()
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
            patient.save()
            return Response({})
