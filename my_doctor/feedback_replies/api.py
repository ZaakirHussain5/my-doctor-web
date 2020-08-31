from .serializers import feedback_repliesSerializer
from .models import feedback_replies
from rest_framework import viewsets, permissions


class feedback_repliesViewSet(viewsets.ModelViewSet):
    queryset = feedback_replies.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = feedback_repliesSerializer