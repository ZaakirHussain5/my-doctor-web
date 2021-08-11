from .serializers import doctor_paymentsSerializer, DoctorPaymentsListSerializer
from .models import doctor_payments
from rest_framework import viewsets, permissions
from doctors.models import doctors_info
from datetime import date
from django.db.models import Sum, Q


def getDateFormat(date_time):
    dates = date_time.split('-')
    year = int(dates[0])
    month = int(dates[1])
    day = int(dates[2])
    d = date( year, month, day )
    # year = '{:02d}'.format(d.year)
    # month = '{:02d}'.format(d.month)
    # day = '{:02d}'.format(d.day)
    # formated_date = '{0}-{1}-{2}'.format(year, month, day)

    return d

class doctor_paymentsViewSet(viewsets.ModelViewSet):
    queryset = doctor_payments.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = doctor_paymentsSerializer


class doctor_listViewset(viewsets.ModelViewSet):
    queryset = doctor_payments.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DoctorPaymentsListSerializer



class doctor_dataView(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = DoctorPaymentsListSerializer
    def get_queryset(self):
        return doctor_payments.objects.filter(doctor__user = self.request.user)




def today_total_doctor_paid():
    today = date.today()
    total_amount = doctor_payments.objects.filter(created_at__contains = today).aggregate(Sum('paid_amount'))
    return total_amount

def in_a_range_dotor_paid(from_time, to_time):
    from_times = getDateFormat(from_time)
    to_times = getDateFormat(to_time)
    total_amount = doctor_payments.objects.filter(created_at__date__range=(from_times, to_times)).aggregate(Sum('paid_amount'))
    return total_amount