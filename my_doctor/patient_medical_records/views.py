from django.shortcuts import render
from django.http import JsonResponse
from .models import patient_medical_records

def get_pres_by_consultation(request):
    cons_id = request.GET.get('cons_id')
    response = {}
    response['pres_avl'] = True
    try:
       prescription = patient_medical_records.objects.get(consultation_id=cons_id)
       response['prescription_file'] = prescription.record_files.url
    except patient_medical_records.DoesNotExist:
       response['pres_avl'] = False

    return JsonResponse(response)
