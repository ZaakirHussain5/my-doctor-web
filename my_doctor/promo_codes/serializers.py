from rest_framework import serializers
from .models import promo_code

class promo_codeSerializer(serializers.ModelSerializer):
    class Meta:
        model = promo_code
        fields = ['id', 'code', 'discount_percent']

