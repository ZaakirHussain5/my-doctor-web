from django.db import models
from django.contrib.auth.models import User
from doctors.models import doctors_info
from patients.models import patient_info
from doctor_payments.models import doctor_payments
from django.db.models import Max

def generateId():
    import datetime
    now = datetime.datetime.now()
    uid = consultations.objects.aggregate(Max('id'))
    uid = uid['id__max'] 
    if uid == None:
        uid = 0
    return 'DPINV'+ str(now.year) + str(uid+1)


class consultations(models.Model):
    doctor_id = models.ForeignKey(doctors_info,related_name='doctor_consulataions',on_delete=models.CASCADE)
    patient = models.ForeignKey(User,related_name='consultations',on_delete=models.SET_NULL,null=True, blank=True)
    consultation_date_time = models.DateTimeField(auto_now_add=True)
    subscription_based = models.BooleanField(default=False)
    inv_number  = models.CharField(max_length=25,default=generateId)
    video_audio_rating = models.IntegerField(default=0)
    consultation_rating = models.IntegerField(default=0)
    overall_rating = models.IntegerField(default=0)
    problem=models.CharField(max_length=250,default='Not Specified')
    message = models.CharField(max_length=500, null=True, blank=True)
    consultation_amt = models.DecimalField(max_digits=10,decimal_places=2, default=0.00)
    comp_share = models.DecimalField(max_digits=10,decimal_places=2,null=True)

    @property
    def patient_name(self):
        try:
            return patient_info.objects.get(user__id=self.patient.id).full_name
        except:
            return "Patient Deleted"
    @property
    def patient_number(self):
        return patient_info.objects.get(user__id=self.patient.id).ph_no

    @property
    def patient_age(self):
        try:
            return patient_info.objects.get(user__id=self.patient.id).age
        except:
            return 0
    @property
    def patient_gender(self):
        try:
            return patient_info.objects.get(user__id=self.patient.id).gender
        except:
            return "No data"
    @property
    def format_date(self):
        return self.consultation_date_time.date()

    def __str__(self):
        return self.doctor_id.full_name + str(self.id)

    def save(self, *args, **kwargs):
        if not doctor_payments.objects.filter(doctor = self.doctor_id):
            doctor_payments.objects.create(doctor = self.doctor_id)
        super().save(*args, **kwargs)
        