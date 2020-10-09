from django.http import JsonResponse
from rest_framework.decorators import api_view
from doctors.models import doctors_info
from patients.models import patient_info
from doctors.serializers import doctors_infoSerializer
from patients.serializers import patient_infoSerializer
from django.db.models import Q
import json

@api_view(['GET'])
def Enquires(request):
    requested_text = request.GET.get('search')
    matched_doctor = doctors_info.objects.filter(Q(Registration_Number__icontains = requested_text) | Q(phone_number__icontains=requested_text) | Q(full_name__icontains=requested_text))
    matched_patient = patient_info.objects.filter( Q(pat_id__icontains = requested_text) | Q(ph_no__icontains=requested_text) | Q(full_name__icontains=requested_text))

    print("Doctor Lits=====", matched_doctor)
    print("Patient Lits=====", matched_patient)

    return JsonResponse({
        'doctors': doctors_infoSerializer(matched_doctor, many=True).data,
        "patients": patient_infoSerializer(matched_patient, many=True).data
    })