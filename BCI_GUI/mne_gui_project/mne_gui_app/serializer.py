from rest_framework import serializers
from .models import *

class ReactSerializer(serializers.ModelSerializer):

	class Meta:
		model = React
		fields = ['name', 'detail']

class EEGDataSerializer(serializers.ModelSerializer):

	class Meta:
		model = EEGData
		fields = '__all__'