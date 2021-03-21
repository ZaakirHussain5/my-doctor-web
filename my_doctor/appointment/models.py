from django.db import models
from django.contrib.auth.models import User
from doctors.models import doctors_info
from patients.models import patient_info
from rest_framework.reverse import reverse

class appointment(models.Model):
    appointment_date = models.CharField(max_length=32)
    appointment_time = models.CharField(max_length=32)
    doctor = models.ForeignKey(doctors_info,on_delete=models.CASCADE)
    patient = models.ForeignKey(User,related_name='appointments',on_delete=models.SET_NULL,null=True)
    Description = models.CharField(max_length=32, null=True)
    paid_amount = models.DecimalField(max_digits=10,decimal_places=2)
    consultation_status = models.CharField(max_length=25, null=True)
    payment_type = models.CharField(max_length=25, null=True)
    payment_id = models.CharField(max_length=25, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=25, null=True)
    Last_modied = models.DateTimeField(auto_now_add=True)
    Modified_by = models.CharField(max_length=25, null=True)
    cancle_note = models.CharField(max_length=500, default='')

    
    @property
    def pat_id(self):
        return patient_info.objects.get(user__id=self.patient.id).id

    @property
    def patient_name(self):
        try:
            return patient_info.objects.get(user__id=self.patient.id).full_name
        except:
            return "Patient Deleted"
    
    @property
    def patient_login_status(self):
        try:
            return patient_info.objects.get(user__id=self.patient.id).is_logged_in
        except:
            return False
    
    @property
    def patient_age(self):
        return patient_info.objects.get(user__id=self.patient.id).age
    
    @property
    def patient_gender(self):
        return patient_info.objects.get(user__id=self.patient.id).gender
    
    @property
    def video_flag(self):
        import datetime
        today = datetime.datetime.now()
        after_15mins = today + datetime.timedelta(minutes=10)
        appointment_time = self.appointment_time
        str_appointment_date = self.appointment_date
        date_format_app_date = datetime.datetime.strptime(str_appointment_date, "%d/%m/%Y")

        day_diff = today - date_format_app_date
        if day_diff.days == 0:
            app_time_instance = datetime.datetime.strptime(str_appointment_date + ' ' + appointment_time, '%d/%m/%Y %I:%M %p')
            diff = (app_time_instance - after_15mins)
            in_secoends = diff.total_seconds()
            if int(in_secoends/600) < 0:
                return True
            else:
                return False
        else:
            return False
    

    def __str__(self):
        return str(self.id)
