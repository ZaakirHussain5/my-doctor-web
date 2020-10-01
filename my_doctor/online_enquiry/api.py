from rest_framework import viewsets,permissions
from .models import online_enquiry
from .serializers import online_enquiry_serializer

class online_enquiryAPI(viewsets.ModelViewSet):
    queryset=online_enquiry.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class=online_enquiry_serializer