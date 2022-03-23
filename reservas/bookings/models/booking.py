"""Customer Model"""
import uuid

from django.db import models
from reservas.utils.models import BookingAudit
from reservas.bookings.models import State
from reservas.customers.models import Customer


class Booking (BookingAudit):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # CheckIn date
    check_in_date = models.DateTimeField(blank=False, null=False)
    # CheckOut date
    check_out_date = models.DateTimeField(blank=False, null=False)
    # State of Payment
    state = models.ForeignKey(State, blank=False, null=False, on_delete=models.PROTECT)
    # Customer Data
    customer = models.ForeignKey(Customer, blank=False, null=False, on_delete=models.PROTECT)
