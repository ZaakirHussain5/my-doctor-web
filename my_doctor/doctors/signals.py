from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import settlement_details
from doctor_payments.models import doctor_payments
from .models import DoctorBillingHistory

@receiver(post_save, sender=settlement_details)
def save_selectment(sender, instance, **kwargs):
    consult = doctor_payments.objects.filter(doctor_id=instance.doctor_id).values_list('balance',flat=True).first()
    paid_amounts = doctor_payments.objects.filter(doctor_id=instance.doctor_id).values_list('paid_amount',flat=True).first()
    print(consult)
    if instance.paid_amount:
        balance = consult - instance.paid_amount
        paid_amounts += instance.paid_amount
    # if paid_amounts:
    else:
        paid_amounts = instance.paid_amount

    doctor_payments.objects.filter(doctor_id=instance.doctor_id).update(balance=balance, paid_amount=paid_amounts)
    DoctorBillingHistory.objects.create(doctor=instance.doctor_id,ref_id=instance.bank_trans_id,e_amt=0,r_amt=instance.paid_amount,balance=balance,description='Settlement NEFT Bank TRf')