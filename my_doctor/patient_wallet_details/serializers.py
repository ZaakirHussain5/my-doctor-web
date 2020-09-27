from rest_framework import serializers
from .models import patient_wallet_details
from transactions.models import transactions
from transactions.serializers import transactionsSerializer
from django.contrib.auth.models import User


class patient_wallet_detailsSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if data.get('patient'):
            if self.instance:
                if patient_wallet_details.objects.filter(patient=data.get('patient')).exclude(id=self.instance.id).exists():
                    raise serializers.ValidationError({'patient': 'Patient already exists'})
            elif patient_wallet_details.objects.filter(patient=data.get('patient')).exists():
                raise serializers.ValidationError({'patient': 'Patient already exists'})
        return data

    class Meta:
        model = patient_wallet_details
        fields = '__all__'

class WalletSerializer(serializers.ModelSerializer):
    wallet = serializers.SerializerMethodField()
    transaction = serializers.SerializerMethodField()

    def get_wallet(self, obj):
        patient, balance = "", ""
        data = {}
        if obj.patient:
            patient = obj.patient.username
        if obj.balance:
            balance = obj.balance
        data = {"id":obj.id, "patient":patient, "balance":balance}
        return data

    def get_transaction(self, obj):
        transactions_list = obj.patient.transaction.filter(user_id__username=obj.patient)
        return transactionsSerializer(transactions_list, many=True).data
        
    class Meta:
        model = patient_wallet_details
        fields = ("wallet","transaction")
