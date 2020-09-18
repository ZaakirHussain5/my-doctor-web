from django.shortcuts import render
from django.http import JsonResponse
from .models import consultations

def generateId(request):
    import datetime
    now = datetime.datetime.now()
    uid = consultations.objects.aggregate(Max('id'))
    uid = uid['id__max'] 
    if uid == None:
        uid = 0
    return JsonResponse({"inv_num":'DPINV'+ str(now.year) + str(uid+1)})
