from .serializers import userSerializer,RegistrationSerializer,UserAuthSerializer,LoginSerializer, socialSerializer
from .models import user_details
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework import viewsets, permissions,generics
from rest_framework import mixins
from doctors.models import doctors_info
from doctors.serializers import doctors_infoSerializer
from patients.models import patient_info
from patients.serializers import patient_infoSerializer
from django.contrib.auth.models import User
from django.contrib.auth import login

class userViewSet(viewsets.ModelViewSet):
    queryset = user_details.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = userSerializer

class RegisterAPI(generics.GenericAPIView):
  serializer_class = RegistrationSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response({
      "user": UserAuthSerializer(user, context=self.get_serializer_context()).data,
      "token": AuthToken.objects.create(user)[1]
    })

class LoginAPI(generics.GenericAPIView):
  serializer_class = LoginSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data
    login(request,user)
    _, token = AuthToken.objects.create(user)
    return Response({
      "user": UserAuthSerializer(user, context=self.get_serializer_context()).data,
      "token": token
    })

class UserAPI(generics.RetrieveAPIView):
  permission_classes = [
    permissions.IsAuthenticated,
  ]
  serializer_class = UserAuthSerializer

  def get_object(self):
    return self.request.user


class g_loginView(generics.GenericAPIView):
  serializer_class = socialSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    login(request,user)
    return Response({
      "user": UserAuthSerializer(user, context=self.get_serializer_context()).data,
      "token": AuthToken.objects.create(user)[1]
    })


class checkEmail(viewsets.ModelViewSet):
  serializer_class= UserAuthSerializer
  permission_classes = [
    permissions.AllowAny,
  ]
  def get_queryset(self):
    data_email = self.request.query_params.get('email', None)
    print('email is ', data_email)
    data_phone = self.request.query_params.get('phone', None)
    if data_email is not None:
      user =  User.objects.filter(email__icontains = data_email)
      return user
    if data_phone is not None:
      doctors = doctors_info.objects.filter(phone_number__icontains=data_phone)
      if doctors.count() > 0:
        self.serializer_class = doctors_infoSerializer
        return doctors
      self.serializer_class = patient_infoSerializer
      patients = patient_info.objects.filter(ph_no__icontains = data_phone)
      return patients 