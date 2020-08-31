from .serializers import executive_detailsSerializer,ExecutiveRegistrationSerializer
from .models import executive_details
from rest_framework import viewsets, permissions,generics
from accounts.serializers import UserAuthSerializer
from rest_framework.response import Response


class executive_detailsViewSet(viewsets.ModelViewSet):
    queryset = executive_details.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = executive_detailsSerializer

class ExecutiveRegistrationAPI(generics.GenericAPIView):
    serializer_class = ExecutiveRegistrationSerializer

    def get_queryset(self):
        return executive_details.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "Executive": UserAuthSerializer(user, context=self.get_serializer_context()).data
        })