from django.urls import path

from meter.views import RegisterMeterCreateView, check_meter_usage, CreateMeterReading, \
    AllMetersListView

urlpatterns = [
    path('add-meter', RegisterMeterCreateView.as_view()),
    path('all-meters', AllMetersListView.as_view()),
    path('meter-usage/<str:meter_id>', check_meter_usage),
    path('create-reading', CreateMeterReading.as_view()),  # new
]
