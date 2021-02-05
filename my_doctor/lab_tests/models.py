from django.db import models
from patients.models import patient_info
from django.db.models import Max

class lab_tests(models.Model):
    title = models.CharField(max_length=120)
    grid_description = models.TextField(null=True,blank=True)
    short_desc =models.TextField(null=True,blank=True)
    detailed_description = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class lab_tests_parameters_type(models.Model):
    lab_test = models.ForeignKey(lab_tests,on_delete=models.CASCADE)
    parameter_type = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class lab_tests_parameter(models.Model):
    parameter_type = models.ForeignKey(lab_tests_parameters_type,on_delete=models.CASCADE, related_name='type_children')
    parameter = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class lab_tests_faqs(models.Model):
    lab_test = models.ForeignKey(lab_tests,on_delete=models.CASCADE)
    question = models.TextField(null=True,blank=True)
    answer =models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def generateOrderId():
    import datetime
    now = datetime.datetime.now()
    uid = lab_tests_purchase.objects.aggregate(Max('id'))
    uid = uid['id__max'] 
    if uid == None:
        uid = 0
    return 'DPLTORD'+ str(now.year) + str(uid+1)

class lab_tests_purchase(models.Model):
    order_id = models.CharField(max_length=123,default=generateOrderId)
    user_id = models.ForeignKey(patient_info,on_delete=models.CASCADE)
    lab_test_id = models.ForeignKey(lab_tests,on_delete=models.SET_NULL,null=True)
    payment_id = models.CharField(max_length=120)
    purchase_date = models.DateTimeField(auto_now_add=True)
    is_delivered = models.BooleanField(default=False)
    report_file = models.FileField(null=True)

    def __str__(self):
        return self.user_id.full_name


