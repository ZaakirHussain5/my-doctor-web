from django.db import models
from django.contrib.auth.models import User

class patient_info(models.Model):
    user = models.OneToOneField(User,related_name='patients',on_delete=models.CASCADE)
    pat_id = models.CharField(max_length=150,unique=True)
    full_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=25, blank=True, null=True)
    dob = models.CharField(max_length=25,null=True, blank=True)
    age = models.CharField(max_length=2,null=True, blank=True)
    blood_group = models.CharField(max_length=5, null=True)
    rel_type = models.CharField(max_length=25,null=True)
    relation = models.CharField(max_length=32,null=True)
    ph_no=models.CharField(max_length=15)
    s_ph_no=models.CharField(max_length=15,null=True)
    pref_lang = models.CharField(max_length=25,null=True)
    street_address = models.CharField(max_length=200,null=True)
    locality = models.CharField(max_length=25,null=True)
    city = models.CharField(max_length=32,null=True)
    pincode=models.CharField(max_length=10,null=True)
    medical_history = models.CharField(max_length=1000,null=True, blank=True)
    other_history=models.CharField(max_length=100,null=True, blank=True)
    groups=models.CharField(max_length=200,null=True, blank=True)
    profile_pic=models.FileField(max_length=355,null=True)
    height=models.CharField(max_length=10,null=True, blank=True)
    weight=models.CharField(max_length=10,null=True, blank=True)
    marital_status=models.CharField(max_length=20,null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    is_logged_in=models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

    @property
    def get_age(self):
        if (self.age != None) and (self.age != ''):
            return self.age
        else:
            return 1

class medical_history(models.Model):
    medical_history=models.CharField(max_length=25)
    def __str__(self):
        return self.medical_history

class groups(models.Model):
    groups=models.CharField(max_length=25)

    def __str__(self):
        return self.groups


class PatientBillingHistory(models.Model):
    patient = models.ForeignKey(patient_info, on_delete=models.CASCADE)
    doc_name = models.CharField(max_length=100,null=True)
    doc_spl = models.CharField(max_length=100,null=True)
    doc_image = models.FileField(null=True)
    amount = models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
    date = models.DateTimeField(auto_now_add = True)
    status=models.CharField(max_length=50)
    description = models.CharField(max_length=100)

class patient_family_members(models.Model):
    patient = models.ForeignKey(patient_info,related_name="Family", on_delete=models.CASCADE,null=True)
    member_name = models.CharField(max_length=50)
    member_relation = models.CharField(max_length=50)
    member_age=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.member_name

