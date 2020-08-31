from django.shortcuts import render
from .models import patient_info
from django.db.models import Max
from django.http import HttpResponse

def generateId(request):
    import datetime
    now = datetime.datetime.now()
    uid = patient_info.objects.aggregate(Max('id'))
    uid = uid if uid is None else 1
    return HttpResponse('DPPAT'+ str(now.year) + str(uid))
