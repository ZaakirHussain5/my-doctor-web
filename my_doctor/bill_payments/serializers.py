from rest_framework import serializers
from .models import BillPayments

class BillPaymentsSeralizers(serializers.ModelSerializer):
    class Meta:
        model = BillPayments
        fields = "__all__"
