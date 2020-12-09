from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import appointment
from patients.models import PatientBillingHistory,patient_info

@receiver(post_save, sender=appointment)
def save_doctor_payment(sender, instance, **kwargs):
    patient = patient_info.objects.get(user=instance.patient)
    if instance.consultation_status != "Cancelled":
        billing_history = PatientBillingHistory.objects.create(patient=patient,status="P",
        description="Amount Deducted for New Appointment",
        amount=instance.paid_amount,doc_name=instance.doctor.full_name,
        doc_image=instance.doctor.profile_pic,doc_spl=instance.doctor.specialist_type)
        billing_history.save()
    else:
        billing_history = PatientBillingHistory.objects.create(patient=patient,status="R",
        description="Amount added to wallet for Appointment Appointment Cancellation",
        amount=instance.paid_amount,doc_name=instance.doctor.full_name,
        doc_image=instance.doctor.profile_pic,doc_spl=instance.doctor.specialist_type)
        billing_history.save()

