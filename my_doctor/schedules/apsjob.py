from appointment.models import appointment
import datetime


def send_todays_message():
    all_pending_appointment = appointment.objects.filter(consultation_status='Pending')
    for appointments in all_pending_appointment:
        today = datetime.datetime.now()
        next_two_day = today + datetime.timedelta(days=2)
        str_appointment_date = appointments.appointment_date
        date_format_app_date = datetime.datetime.strptime(str_appointment_date, "%d/%m/%Y")
        diff = next_two_day - date_format_app_date
        if diff.days >= 0:
            pass
            #https://teleduce.in/sendsms/?key=a224db72-cafb-4cce-93ab-3d7f950c92e2&text=Your Appointment with Dr. DoctorName has been fixed for today at ${response.appointment_time} to keep track of your appointments visit https://doctor-plus.in/patients/appointments &route=0&from=BANDSS&to=${$('#ph_no').val()}


# def send_message_before_15mins():
#     all_pending_appointment = appointment.objects.filter(consultation_status='Pending')
#     for appointments in all_pending_appointment:
#         today = datetime.datetime.now()
