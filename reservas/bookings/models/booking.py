"""Customer Model"""
import uuid

from django.db import models
from reservas.utils.models import BookingAudit
from reservas.bookings.models import State, PaymentMethod
from reservas.customers.models import Customer
from reservas.rooms.models import Room


class Booking (BookingAudit):
    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # CheckIn date
    check_in_date = models.DateTimeField(blank=False, null=False)
    # CheckOut date
    check_out_date = models.DateTimeField(blank=False, null=False)
    # Calc Amount
    amount = models.DecimalField(max_digits=6, decimal_places=2, default=1)
    # Payment Method
    payment_method = models.ForeignKey(PaymentMethod, blank=True, null=True, on_delete=models.PROTECT)
    # State of Payment
    state = models.ForeignKey(State, blank=True, null=True, on_delete=models.PROTECT, default='PEN')
    # Customer Data
    customer = models.ForeignKey(Customer, blank=False, null=False, on_delete=models.PROTECT)
    # Room Data
    room = models.ForeignKey(Room, blank=False, null=False, on_delete=models.PROTECT)
