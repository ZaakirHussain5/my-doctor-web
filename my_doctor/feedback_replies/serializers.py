from rest_framework import serializers
from .models import feedback_replies


class feedback_repliesSerializer(serializers.ModelSerializer):
    class Meta:
        model = feedback_replies
        fields = '__all__'