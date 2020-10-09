from rest_framework import serializers
from django.contrib.auth.models import User


class QueriesSerializers(serializers.modelSerilizer):
	
	
	class Meta:
		model = User