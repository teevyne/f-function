from django.db import models


class RegisterMeter(models.Model):
    meter_id = models.CharField(max_length=10)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)


class MeterReading(models.Model):
    meter = models.CharField(max_length=10)
    meter_reading = models.IntegerField()
    date_sent = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meter


class CurrentUsage(models.Model):
    meter = models.CharField(max_length=10)
    total_power_used = models.CharField(max_length=10)
    power_remaining = models.CharField(max_length=10)

    def __str__(self):
        return self.meter
