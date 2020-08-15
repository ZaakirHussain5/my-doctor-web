from .serializers import userSerializer,RegistrationSerializer,UserAuthSerializer,LoginSerializer
from .models import user_details
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework import viewsets, permissions,generics

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
