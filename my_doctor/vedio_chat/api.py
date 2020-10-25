from rest_framework import permissions,viewsets, mixins
from .models import VedioChat
from .serializers import VedioChatSerializer

class vedioChatOparetion(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = VedioChatSerializer

    def get_queryset(self):
        return VedioChat.objects.all()
    
    def perform_create(self,serializer):
        return serializer.save()    