from rest_framework import permissions,viewsets
from .models import Reminders
from .serializers import RemindersSerializer



class reminders_api(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = RemindersSerializer
    # get request for getting all reminders.

    def get_queryset(self):
        return self.request.user.reminders.all()

    def perform_create(self,serializer):
        return serializer.save(reminder_owner=self.request.user)

    def perform_update(self, serializer):
        return serializer.save(rem)