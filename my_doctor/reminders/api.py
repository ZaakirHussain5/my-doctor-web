from rest_framework import permissions,viewsets, mixins
from .models import Reminders
from .serializers import RemindersSerializer
from datetime import datetime


class reminders_api(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = RemindersSerializer
    # get request for getting all reminders.

    def get_queryset(self):
        date  = self.request.GET.get('date').split( )
        date_format = datetime.strptime(date[1], '%b')
        date_str = str(date[-1]) + '-'+ str(date_format.month)+ '-' + str(date[-2]) 
        print('=======', date_str)
        dates = datetime.strptime(date_str, "%Y-%m-%d")
        return self.request.user.reminders.filter(reminder_date=dates)

    def perform_create(self,serializer):
        
        return serializer.save(reminder_owner=self.request.user)

    
class remindersList(mixins.ListModelMixin):
    serializer_class = RemindersSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        queryset = self.request.user.reminders.all()
        selected_data = self.request.query_params.get('date', None)
        if selected_data is not None:
            # queryset = queryset.filter
            pass