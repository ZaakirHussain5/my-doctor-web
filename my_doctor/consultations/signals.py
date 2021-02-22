from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from consultations.models import consultations
from doctor_payments.models import doctor_payments
from doctors.models import settlement_details, doctors_info, DoctorBillingHistory
from patients.models import patient_info

@receiver(post_save, sender=consultations)
def save_doctor_payment(sender, instance, created, **kwargs):
    if created:
        total_amount = doctor_payments.objects.filter(doctor = instance.doctor_id).values_list('total_amt',flat=True).first()
        balance = doctor_payments.objects.filter(doctor = instance.doctor_id).values_list('balance',flat=True).first()
        commission_amount = doctor_payments.objects.filter(doctor = instance.doctor_id).values_list('comm_amt',flat=True).first()
        print(instance)
        if instance.comp_share >= 0.0:
            if total_amount:
                total_amount = total_amount + instance.doctor_id.consultation_fee
            else:
                total_amount = instance.doctor_id.consultation_fee
            if commission_amount:
                commission_amount = commission_amount + instance.comp_share
            else:
                commission_amount = instance.comp_share
            payable = float(total_amount) - float(commission_amount)
            if balance:
                add_new_amount = float(instance.doctor_id.consultation_fee) 
                balance = float(balance) + float(add_new_amount)
            else:
                balance = float(payable)
        patient = patient_info.objects.get(user=instance.patient)
        billing_history = DoctorBillingHistory.objects.create(doctor=instance.doctor_id,ref_id=patient.pat_id,e_amt=instance.doctor_id.consultation_fee,r_amt=0,balance=balance,description='Consultation Fee')
        doc_count = consultations.objects.filter(doctor_id = instance.doctor_id).count()
        payments = doctor_payments.objects.filter(doctor = instance.doctor_id).update(total_amt=total_amount, consultations_count=doc_count, comm_amt=commission_amount, amount_payable=payable, balance=balance)
        
