# Generated by Django 3.2.10 on 2021-12-10 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentUsage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meter', models.CharField(max_length=10)),
                ('power_used', models.CharField(max_length=10)),
                ('power_remaining', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MeterReading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meter', models.CharField(max_length=10)),
                ('meter_reading', models.IntegerField()),
                ('date_sent', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterMeter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meter_id', models.CharField(max_length=10)),
                ('date_added', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
