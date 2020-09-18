from django.db import models
from django.contrib.auth.models import User
from doctors.models import doctors_info

class consultations(models.Model):
    doctor_id = models.ForeignKey(doctors_info,related_name='doctor_consulataions',on_delete=models.CASCADE)
    patient = models.ForeignKey(User,related_name='consultations',on_delete=models.SET_NULL,null=True)
    consultation_date_time = models.DateTimeField(auto_now_add=True)
    subscription_based = models.BooleanField(default=False)
    inv_number  = models.CharField(max_length=25, null=True)
    video_audio_rating = models.IntegerField()
    consultation_rating = models.IntegerField()
    overall_rating = models.IntegerField()
    message = models.CharField(max_length=500, null=True)
    duration = models.CharField(max_length=100)
    consultation_amt = models.DecimalField(max_digits=10,decimal_places=2)
    comp_share = models.DecimalField(max_digits=10,decimal_places=2,null=True)

    def __str__(self):
        return self.doctor_id