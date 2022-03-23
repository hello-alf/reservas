from django.urls import re_path
from reservas.bookings.views import BookingAPIView

app_name = "rooms"
urlpatterns = [
    re_path(r'^v1/bookings/', BookingAPIView.as_view(), name='booking_action'),
]
