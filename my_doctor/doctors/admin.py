from django.contrib import admin
from .models import DoctorBillingHistory, doctors_info,DoctorTimings, settlement_details, DoctorBankDetails
# Register your models here.

admin.site.register(doctors_info)
admin.site.register(DoctorTimings)
admin.site.register(settlement_details)
admin.site.register(DoctorBankDetails)
admin.site.register(DoctorBillingHistory)