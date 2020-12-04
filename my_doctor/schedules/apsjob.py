import datetime
import requests
from appointment.models import appointment
from patients.models import patient_info


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
            app_time_instance = datetime.datetime.strptime(str_appointment_date + ' ' + appointment_time, '%d/%m/%Y %H:%M %p')
            diff = (app_time_instance - after_15mins)
            in_secoends = diff.total_seconds()
            if int(in_secoends/60) == 0:
                patient = patient_info.objects.get(user=appointments.patient)
                url = "https://teleduce.in/sendsms/?key=a224db72-cafb-4cce-93ab-3d7f950c92e2&text=Your Appointment with Dr. {0} has been next 15 minutes later to keep track of your appointments visit https://doctor-plus.in/patients/appointments &route=0&from=BANDSS&to={1}".format(appointments.doctor.full_name, patient.ph_no)
                requests.get(url)