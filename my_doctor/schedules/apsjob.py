from appointment.models import appointment
import datetime


def send_todays_message():
    all_pending_appointment = appointment.objects.filter(consultation_status='Pending')
    for appointments in all_pending_appointment:
        today = datetime.datetime.now()
        
        str_appointment_date = appointments.appointment_date
        date_format_app_date = datetime.datetime.strptime(str_appointment_date, "%d/%m/%Y")
        diff = today - date_format_app_date
        if diff.days >= 0:
            pass
            #https://teleduce.in/sendsms/?key=a224db72-cafb-4cce-93ab-3d7f950c92e2&text=Your Appointment with Dr. DoctorName has been fixed for today at ${response.appointment_time} to keep track of your appointments visit https://doctor-plus.in/patients/appointments &route=0&from=BANDSS&to=${$('#ph_no').val()}


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
                pass
                #https://teleduce.in/sendsms/?key=a224db72-cafb-4cce-93ab-3d7f950c92e2&text=Your Appointment with Dr. DoctorName has been fixed for today at ${response.appointment_time} to keep track of your appointments visit https://doctor-plus.in/patients/appointments &route=0&from=BANDSS&to=${$('#ph_no').val()}
