from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import appointment
from patients.models import PatientBillingHistory,patient_info
from patient_subscription.models import PatientSubscription

@receiver(post_save, sender=appointment)
def save_doctor_payment(sender, instance, **kwargs):
        patient = patient_info.objects.get(user=instance.patient)
        try:
            pat_subs = PatientSubscription.objects.get(user=patient)
            if pat_subs.is_senior == False:
                if pat_subs.is_active:
                    if instance.consultation_status == "Cancelled":
                        if pat_subs.cons_count == pat_subs.total_count:
                            return
                        if pat_subs.cons_count == 0:
                            pat_subs.is_active = True

                        pat_subs.cons_count = pat_subs.cons_count + 1
                        pat_subs.save()
                    else:
                        if pat_subs.cons_count == 1:
                            pat_subs.is_active = False
                        pat_subs.cons_count = pat_subs.cons_count - 1
                        
                        pat_subs.save()
                    return
        except PatientSubscription.DoesNotExist:
            pass
        if instance.consultation_status == "Completed":
            billing_history = PatientBillingHistory.objects.create(patient=patient,status="P",
            description="Amount Paid for New Appointment",
            amount=instance.paid_amount,doc_name=instance.doctor.full_name,
            doc_image=instance.doctor.profile_pic,doc_spl=instance.doctor.specialist_type)
        elif instance.consultation_status == "Cancelled":
            billing_history = PatientBillingHistory.objects.create(patient=patient,status="R",
            description="Amount added to wallet for Appointment Cancellation",
            amount=instance.paid_amount,doc_name=instance.doctor.full_name,
            doc_image=instance.doctor.profile_pic,doc_spl=instance.doctor.specialist_type)
        elif instance.consultation_status == "Expired":
            billing_history = PatientBillingHistory.objects.create(patient=patient,status="R",
            description="Amount added to wallet for Appointment Expired",
            amount=instance.paid_amount,doc_name=instance.doctor.full_name,
            doc_image=instance.doctor.profile_pic,doc_spl=instance.doctor.specialist_type)

