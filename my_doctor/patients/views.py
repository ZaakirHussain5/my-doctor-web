from django.shortcuts import render
from .models import patient_info
from django.db.models import Max
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from my_doctor.settings import EMAIL_HOST_USER


def generateId(request):
    import datetime
    now = datetime.datetime.now()
    uid = patient_info.objects.aggregate(Max('id'))
    uid = uid['id__max'] 
    if uid == None:
        uid = 0
    return JsonResponse({"pat_id":'DPPAT'+ str(now.year) + str(uid+1)})


def send_mails(request):
    mail_subject = 'Activate your account.'
    message = render_to_string('email.html', {
        'username': "Zaakir ",
        'patient_id': "DPAT20202",
        'password': '1234'
    })

    msg = EmailMessage(
        'Subject',
        message,
        EMAIL_HOST_USER,
        ['ssamiran472@gmail.com', 'dragndrop111@gmail.com'],
    )
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()
    return redirect('dashboard')