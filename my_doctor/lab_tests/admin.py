from django.contrib import admin
from .models import lab_tests,lab_tests_purchase, lab_test_perches_files
# Register your models here.

admin.site.register(lab_tests)
admin.site.register(lab_tests_purchase)
admin.site.register(lab_test_perches_files)



