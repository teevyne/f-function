from rest_framework import serializers
from .models import MeterReading, CurrentUsage, RegisterMeter


class MeterReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeterReading
        fields = '__all__'


class CurrentUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentUsage
        fields = '__all__'


class RegisterMeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterMeter
        fields = '__all__'
