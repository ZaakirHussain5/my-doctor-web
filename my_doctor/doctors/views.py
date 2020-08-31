from django.shortcuts import render
from .models import doctors_info
from django.db.models import Max
from django.http import HttpResponse

def generateId(request):
    import datetime
    now = datetime.datetime.now()
    uid = doctors_info.objects.aggregate(Max('id'))
    uid = uid['id__max'] 
    if uid == None:
        uid = 0
    return HttpResponse('DPDOC'+ str(now.year) + str(uid+1))
