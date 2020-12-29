from patient_subscription.models import PatientSubscription
from datetime import date

def check_subscription():
    subscripted_plan = PatientSubscription.objects.filter(is_active=True)
    for plan in subscripted_plan:
        if plan.end_date == date.today:
            plan.is_active = False
            plan.save()
