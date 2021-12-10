import datetime

from django.db.models import F
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CurrentUsage, RegisterMeter, MeterReading
from .serializers import MeterReadingSerializer, CurrentUsageSerializer, RegisterMeterSerializer


class RegisterMeterCreateView(generics.CreateAPIView):
    queryset = RegisterMeter.objects.all()
    serializer_class = RegisterMeterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

        meter = request.data.get('meter_id')

        payload = {
            "meter": meter,
            "total_power_used": "0",
            "power_remaining": "0",
        }

        CurrentUsage.objects.create(**payload)

        if serializer.is_valid():
            serializer.save()

        return Response({"message": "Meter has been on-boarded and a default current reading created"},
                        status=status.HTTP_200_OK)


@api_view(['GET'])
def check_meter_usage(self, meter_id):
    meter_reading = CurrentUsageSerializer(CurrentUsage.objects.get(meter=meter_id))
    return Response(meter_reading.data)


class CreateMeterReading(generics.CreateAPIView):   # New
    queryset = MeterReading.objects.all()
    serializer_class = MeterReadingSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

        meter = request.data.get('meter')
        meter_reading = int(request.data.get('meter_reading'))

        meter_usage_object = CurrentUsage.objects.get(meter=meter)
        CurrentUsage.objects.filter(meter=meter_usage_object.meter).update(
            total_power_used=F("total_power_used") + meter_reading,
            power_remaining=25 - (F("total_power_used") + meter_reading)
        )

        meter_usage_object.refresh_from_db()

        if serializer.is_valid():
            serializer.save()
        return Response({"message": "Reading created, current usage updated"}, status=status.HTTP_200_OK)


class AllMetersListView(generics.ListAPIView):
    queryset = RegisterMeter.objects.all()
    serializer_class = RegisterMeterSerializer
