from django.http import JsonResponse
from rest_framework.decorators import api_view
from doctors.models import doctors_info
from patients.models import patient_info
from doctors.serializers import doctors_listSerializer
from patients.serializers import patient_infoSerializer
from django.db.models import Q
import json
from appointment.api import get_a_range_appointment
from doctor_payments.api import in_a_range_dotor_paid
from consultations.api import range_of_collected_comission

@api_view(['GET'])
def SearchAPI(request):
    requested_text = request.query_params.get('q')
    matched_doctor = doctors_info.objects.filter(Q(user__username__icontains = requested_text) | Q(phone_number__icontains=requested_text) | Q(full_name__icontains=requested_text))
    matched_patient = patient_info.objects.filter(Q(user__username__icontains = requested_text) |  Q(pat_id__icontains = requested_text) | Q(ph_no__icontains=requested_text) | Q(full_name__icontains=requested_text))
    return JsonResponse({
        'doctors': doctors_listSerializer(matched_doctor, many=True).data,
        "patients": patient_infoSerializer(matched_patient, many=True).data
    })

@api_view(['GET'])
def snap_shots(request):
    from_date = request.query_params.get('from')
    to_date = request.query_params.get('to')
    appointments_count = get_a_range_appointment(from_date, to_date)
    total_dotor_paid = in_a_range_dotor_paid(from_date, to_date)
    print(total_dotor_paid)
    total_commission = range_of_collected_comission(from_date, to_date)
    return JsonResponse({'appointments_count': appointments_count['total_count'], 'fees': appointments_count['total_fees']['paid_amount__sum'], 'doctor_payout': total_dotor_paid['paid_amount__sum'], "commisions": total_commission['comp_share__sum']})