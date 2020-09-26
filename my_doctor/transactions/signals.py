from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from transactions.models import transactions
from patient_wallet_details.models import patient_wallet_details

@receiver(post_save, sender=transactions)
def save_wallet(sender, instance, **kwargs):
    balance = patient_wallet_details.objects.filter(patient=instance.user_id).values_list('balance',flat=True)
    if instance.credit:
        if balance:
            balance = balance.first() + instance.credit
        else:
            balance = instance.credit
        user = patient_wallet_details.objects.filter(patient=instance.user_id).update(balance=balance)
    elif instance.debit:
        if balance:
            balance = balance.first() - instance.debit
        else:
            balance = instance.debit
        user = patient_wallet_details.objects.filter(patient=instance.user_id).update(balance=balance)
    transactions.objects.filter(id=instance.id).update(balance=balance)