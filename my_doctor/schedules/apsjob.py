import datetime
import requests
from appointment.models import appointment
from patients.models import patient_info
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from my_doctor.settings import EMAIL_HOST_USER
from reminders.models import Reminders
import asyncio

def send_todays_message():
    all_pending_appointment = appointment.objects.filter(consultation_status='Pending')
    for appointments in all_pending_appointment:
        today = datetime.datetime.now()
        
        str_appointment_date = appointments.appointment_date
        date_format_app_date = datetime.datetime.strptime(str_appointment_date, "%d/%m/%Y")
        diff = today - date_format_app_date
        if diff.days >= 0:
            # doctor name, appointment_time, phone_number
            patient = patient_info.objects.get(user=appointments.patient)
            url = "https://teleduce.in/sendsms/?key=a224db72-cafb-4cce-93ab-3d7f950c92e2&text=Your Appointment with Dr. {0} has been fixed for today at {1} to keep track of your appointments visit https://doctor-plus.in/patients/appointments &route=0&from=BANDSS&to={2}".format(appointments.doctor.full_name, appointments.appointment_time, patient.ph_no)
            requests.get(url)
            doct_url = "https://teleduce.in/sendsms/?key=a224db72-cafb-4cce-93ab-3d7f950c92e2&text=Your Appointment with Mr./Mrs {0} has been fixed for today at {1} to keep track of your appointments visit https://doctor-plus.in/patients/appointments &route=0&from=BANDSS&to={2}".format(appointments.patient.full_name, appointments.appointment_time, appointment.doctor.phone_number)
            requests.get(doct_url)

            send_mails(appointments)

#  SEND MESSAGE TO DOCTOR ALSO..
# SEND MESSAGES AT 10mins, 5 mins, 15mins
# ADD INSTANCE OF REMINDER MODEL

async def send_mails(obj):
    patient = patient_info.objects.get(user=obj.patient)
    mail_subject = 'New Appointment.'
    message = render_to_string('emails/reminder1.html', {
        'full_name': patient.full_name,
        'doctor': obj.doctor.full_name,
        "date": obj.appointment_date,
        "time": obj.appointment_time,
    })

    msg = EmailMessage(
        mail_subject,
        message,
        'Doctor Plus <'+ EMAIL_HOST_USER + '>',
        [patient.user.email],
    )
    msg.content_subtype = "html"  # Main content is now text/html
    await msg.send()

    return True


async def reminder_min(obj):
    patient = patient_info.objects.get(user=obj.patient)
    mail_subject = 'New Appointment.'
    message = render_to_string('emails/reminder2.html', {
        'full_name': patient.full_name,
        "doctor": obj.doctor.full_name
    })

    msg = EmailMessage(
        mail_subject,
        message,
        'Doctor Plus <'+ EMAIL_HOST_USER + '>',
        [patient.user.email],
    )
    msg.content_subtype = "html"  # Main content is now text/html
    await msg.send()

    return True

def send_message_before_15mins():
    all_pending_appointment = appointment.objects.filter(consultation_status='Pending')
    today = datetime.datetime.now()
    for appointments in all_pending_appointment:
        after_15mins = today + datetime.timedelta(minutes=15)
        appointment_time = appointments.appointment_time
        str_appointment_date = appointments.appointment_date
        date_format_app_date = datetime.datetime.strptime(str_appointment_date, "%d/%m/%Y")

        day_diff = today - date_format_app_date
        if day_diff.days == 0:
            app_time_instance = datetime.datetime.strptime(str_appointment_date + ' ' + appointment_time, '%d/%m/%Y %I:%M %p')
            diff = (app_time_instance - after_15mins)
            in_secoends = diff.total_seconds()

            if int(in_secoends/900) == 0:
                pat_message = "Your Appointment with Dr. {0} has been next 15 minutes later to keep track of your appointments visit https://doctor-plus.in/patients/appointments".format(appointments.doctor.full_name)
                doct_message = "Your Appointment with Mr./Mrs. {0} has been next 15 minutes later to keep track of your appointments visit https://doctor-plus.in/doctors/appointments".format(patient.full_name)
                pat_reminder = Reminders(message=pat_message, reminder_owner=appointments.patient, appointment_id=appointments.id)
                pat_reminder.save()

                doct_reminder = Reminders(message=doct_message, reminder_owner=appointment.doctor.user, appointment_id=appointments.id )
                doct_reminder.save()
                patient = patient_info.objects.get(user=appointments.patient)
                url = "https://teleduce.in/sendsms/?key=a224db72-cafb-4cce-93ab-3d7f950c92e2&text=Your Appointment with Dr. {0} has been next 15 minutes later to keep track of your appointments visit https://doctor-plus.in/patients/appointments &route=0&from=BANDSS&to={1}".format(appointments.doctor.full_name, patient.ph_no)
                requests.get(url)
                doct_url = "https://teleduce.in/sendsms/?key=a224db72-cafb-4cce-93ab-3d7f950c92e2&text=Your Appointment with Mr./Mrs. {0} has been next 15 minutes later to keep track of your appointments visit https://doctor-plus.in/patients/appointments &route=0&from=BANDSS&to={1}".format(patient.full_name, appointments.doctor.phone_number)
                requests.get(doct_url)
                reminder_min(appointments)

def send_message_before_10mins():
    all_pending_appointment = appointment.objects.filter(consultation_status='Pending')
    today = datetime.datetime.now()
    for appointments in all_pending_appointment:
        after_15mins = today + datetime.timedelta(minutes=10)
        appointment_time = appointments.appointment_time
        str_appointment_date = appointments.appointment_date
        date_format_app_date = datetime.datetime.strptime(str_appointment_date, "%d/%m/%Y")

        day_diff = today - date_format_app_date
        if day_diff.days == 0:
            app_time_instance = datetime.datetime.strptime(str_appointment_date + ' ' + appointment_time, '%d/%m/%Y %I:%M %p')
            diff = (app_time_instance - after_15mins)
            in_secoends = diff.total_seconds()
            if int(in_secoends/600) == 0:
                pat_message = "Your Appointment with Dr. {0} has been next 10 minutes later to keep track of your appointments visit https://doctor-plus.in/patients/appointments".format(appointments.doctor.full_name)
                pat_message = "Your Appointment with Mr./Mrs. {0} has been next 10 minutes later to keep track of your appointments visit https://doctor-plus.in/doctors/appointments".format(patient.full_name)
                pat_reminder = Reminders(message=pat_message, reminder_owner=appointments.patient, appointment_id=appointments.id)
                pat_reminder.save()
                doct_reminder = Reminders(message=doct_message, reminder_owner=appointment.doctor.user, appointment_id=appointments.id )
                doct_reminder.save()

                patient = patient_info.objects.get(user=appointments.patient)
                url = "https://teleduce.in/sendsms/?key=a224db72-cafb-4cce-93ab-3d7f950c92e2&text=Your Appointment with Dr. {0} has been next 10 minutes later to keep track of your appointments visit https://doctor-plus.in/patients/appointments &route=0&from=BANDSS&to={1}".format(appointments.doctor.full_name, patient.ph_no)
                requests.get(url)
                doct_url = "https://teleduce.in/sendsms/?key=a224db72-cafb-4cce-93ab-3d7f950c92e2&text=Your Appointment with Mr./Mrs. {0} has been next 10 minutes later to keep track of your appointments visit https://doctor-plus.in/doctors/appointments &route=0&from=BANDSS&to={1}".format(patient.full_name, appointments.doctor.phone_number)
                requests.get(doct_url)
                reminder_min(appointments)

def send_message_before_5mins():
    all_pending_appointment = appointment.objects.filter(consultation_status='Pending')
    today = datetime.datetime.now()
    for appointments in all_pending_appointment:
        after_15mins = today + datetime.timedelta(minutes=5)
        appointment_time = appointments.appointment_time
        str_appointment_date = appointments.appointment_date
        date_format_app_date = datetime.datetime.strptime(str_appointment_date, "%d/%m/%Y")

        day_diff = today - date_format_app_date
        if day_diff.days == 0:
            app_time_instance = datetime.datetime.strptime(str_appointment_date + ' ' + appointment_time, '%d/%m/%Y %I:%M %p')
            diff = (app_time_instance - after_15mins)
            in_secoends = diff.total_seconds()
            if int(in_secoends/(60*5)) == 0:
                patient = patient_info.objects.get(user=appointments.patient)

                pat_message = "Your Appointment with Dr. {0} has been next 5 minutes later to keep track of your appointments visit https://doctor-plus.in/patients/appointments".format(appointments.doctor.full_name)
                doct_message = "Your Appointment with Mr./Mrs. {0} has been next 5 minutes later to keep track of your appointments visit https://doctor-plus.in/doctors/appointments".format(patient.full_name)
                pat_reminder = Reminders(reminder_message=pat_message, reminder_owner=appointments.patient, appointment_id=appointments.id)
                pat_reminder.save()

                doct_reminder = Reminders(reminder_message=doct_message, reminder_owner=appointments.doctor.user, appointment_id=appointments.id )
                doct_reminder.save()

                url = "https://teleduce.in/sendsms/?key=a224db72-cafb-4cce-93ab-3d7f950c92e2&text=Your Appointment with Dr. {0} has been next 5 minutes later to keep track of your appointments visit https://doctor-plus.in/patients/appointments &route=0&from=BANDSS&to={1}".format(appointments.doctor.full_name, patient.ph_no)
                requests.get(url)
                doct_url = "https://teleduce.in/sendsms/?key=a224db72-cafb-4cce-93ab-3d7f950c92e2&text=Your Appointment with Mr./Mrs. {0} has been next 5 minutes later to keep track of your appointments visit https://doctor-plus.in/doctors/appointments &route=0&from=BANDSS&to={1}".format(patient.full_name, appointments.doctor.phone_number)
                requests.get(doct_url)
                reminder_min(appointments)



# import requests
# import json
# url = "http://teleduce.corefactors.in/send-email-json-otom/xxxxxxxxxxxxxxxxxxx/route/"
# to_list=[{"email_id":"samiransarkar513@gmail.com"}]
# message = {
# "html_content":"<html><head><title></title></head><body><div class='container mt-5 pl-5 pr-5'><div style='color: white; text-align: center; padding: .5rem; background: #2a426c;'><h3 style='font-size: 20px;'>Doctor Plus <sup><span style=' border: 1px solid; border-radius: 50%; padding: .25rem;'>R</span></sup></h3></div><div style='margin: 0 2rem;'><h2><b>Dear {{full_name }},</b></h2><br><h4>Your appointment with {{doctor }} on {{date }} at {{time}}.</h4><br></div><hr><div class='info text-muted'><p>To login click <a href='https://www.doctor-plus.in/login' class='text-justify'>here. </a></p></div><div style='color: white; text-align: center; padding: .5rem; background: #8dc73f ;'><h3>A simple and easy way to consult Doctors Online.</h3></div></div></body></html>",
# "subject":"teleducxxxxxxxxxx",
# "from_mail":"Texxxxx@corefactors.in",
# "from_name":"Testxx",
# "reply_to":"corexxxx@gmail.com",
# "to_recipients":to_list
# }
# payload = {"message" :message}
# single_content = {"mail_datas":payload}
# reqdata = requests.post(url, data=json.dumps(single_content), headers={'Content-Type': 'application/json'})
# print (reqdata.content)