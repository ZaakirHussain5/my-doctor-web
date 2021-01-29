from django.db import models
from django.contrib.auth.models import User

class doctors_info(models.Model):
    user = models.OneToOneField(User,related_name='Doctors',on_delete=models.CASCADE)
    full_name=models.CharField(max_length=32,null=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True)
    commission_val=models.DecimalField(max_digits=10,decimal_places=2,default=59)
    commission_type=models.CharField(max_length=15,default='Amount', null=True)
    gender=models.CharField(max_length=6, default='male', null = True)
    Registration_Number = models.CharField(max_length=25, default='')
    specialist_type = models.CharField(max_length=25, null=True)
    rating = models.FloatField(default=0)
    consultation_fee = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    profile_pic = models.FileField(max_length=355, null=True)
    mou_file = models.FileField(null=True)
    about = models.CharField(max_length=500, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=25, null=True)
    Last_modied = models.DateTimeField(auto_now=True)
    Modified_by = models.CharField(max_length=25, null=True)
    is_loggedin = models.BooleanField(default=False)
    web_registration = models.BooleanField(default=False)
    settlement_cycle = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.full_name) +','+ str(self.specialist_type)

#doctor timings
class DoctorTimings(models.Model):
    doctor=models.ForeignKey(doctors_info,related_name="timings",on_delete=models.CASCADE)
    day = models.CharField(max_length = 10, null=True)
    from_time=models.CharField(max_length=50)
    to_time=models.CharField(max_length=50)

    def __str__(self):
        return self.doctor.full_name



class settlement_details (models.Model):
    doctor_id = models.ForeignKey(doctors_info, on_delete=models.CASCADE, related_name='settlementDoctor')
    paid_amount = models.IntegerField()
    paid_date = models.DateField(auto_now_add=True)
    bank_trans_id = models.CharField(max_length=100, null=True, blank=True)
    


class DoctorBankDetails(models.Model):
    doctor_id = models.ForeignKey(doctors_info, on_delete=models.CASCADE, related_name='DoctorBankDetails')
    account_no = models.CharField(max_length=20, null=True, blank=True)
    ifsc_no = models.CharField(max_length=100, null=True, blank=True)
    bank_name = models.CharField(max_length=50, null=True, blank=True)
    branch_name = models.CharField(max_length=50, null=True, blank=True)
    account_holder_name = models.CharField(max_length=50, null=True, blank=True)
    upi_id = models.CharField(max_length = 50, null=True, blank=True)
    phone_no = models.CharField(max_length = 50,null=True, blank=True)
    blank_cheque = models.FileField(null=True, blank=True)


class Doctornotes(models.Model):
    doctor = models.ForeignKey(doctors_info, on_delete=models.CASCADE)
    notes = models.TextField()

class DoctorBillingHistory(models.Model):
    doctor = models.ForeignKey(doctors_info, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    ref_id = models.CharField(max_length=250,null=True,blank=True)
    e_amt=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    r_amt=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    balance=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    description = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.description
