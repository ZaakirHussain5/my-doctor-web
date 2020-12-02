from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from transactions.models import transactions
from patient_wallet_details.models import patient_wallet_details

@receiver(post_save, sender=transactions)
def save_wallet(sender, instance, **kwargs):
    balance = patient_wallet_details.objects.filter(patient=instance.user_id).values_list('balance',flat=True)
    print(balance)
    if instance.credit:
        print('signals called')
        if len(balance) >0:
            balance = balance.first() + instance.credit
            user = patient_wallet_details.objects.filter(patient=instance.user_id).update(balance=balance)
        else:
            balance = instance.credit
            pat_wallet = patient_wallet_details(patient=instance.user_id, balance=balance)
            pat_wallet.save()
    elif instance.debit:
        if len(balance) >0:
            balance = balance.first() - instance.debit
            user = patient_wallet_details.objects.filter(patient=instance.user_id).update(balance=balance)
        else:
            balance = instance.debit
            user = patient_wallet_details(patient=instance.user_id, balance=balance)
            user.save()
    transactions.objects.filter(id=instance.id).update(balance=balance)