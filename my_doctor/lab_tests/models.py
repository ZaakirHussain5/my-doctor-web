from django.db import models

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
    parameter_type = models.ForeignKey(lab_tests_parameters_type,on_delete=models.CASCADE)
    parameter = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class lab_tests_faqs(models.Model):
    lab_test = models.ForeignKey(lab_tests,on_delete=models.CASCADE)
    question = models.TextField(null=True,blank=True)
    answer =models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)