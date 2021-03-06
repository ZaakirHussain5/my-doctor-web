from django.shortcuts import render
from .models import doctors_info
from .serializers import doctors_infoSerializer
from django.db.models import Max
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random


def generateId(request):
    import datetime
    now = datetime.datetime.now()
    uid = doctors_info.objects.aggregate(Max('id'))
    randNum = random.SystemRandom().choice([i for i in range(1000,9999)])
    uid = uid['id__max'] 
    if uid == None:
        uid = 0

    return JsonResponse({'doctorId': 'DPDOC'+ str(randNum) + str(now.year) + str(uid+1)})

@api_view(['POST'])
def change_mouFile(request):
    if request.user.is_authenticated:
        mou_files = request.data['mou_file']
        doctor = doctors_info.objects.get(user=request.user)
        if doctor.mou_file:
            doctor.mou_file.delete()
        doctor.mou_file = mou_files
        doctor.save()
        serializer = doctors_infoSerializer(doctor)
        return Response(serializer.data)


@api_view(['POST'])
def change_mouFile_for_admin(request):
    # if request.user.is_authenticated:
    mou_files = request.data['mou_file']

    doctor = doctors_info.objects.get(id=request.data['user'])
    if doctor.mou_file:
        doctor.mou_file.delete()
    doctor.mou_file = mou_files
    doctor.save()
    serializer = doctors_infoSerializer(doctor)
    return Response(serializer.data)

