"""Customer Model"""

from django.db import models
from reservas.utils.models import BookingAudit


class Room (BookingAudit):
    room_id = models.AutoField(primary_key=True)
    # Room number
    number = models.PositiveSmallIntegerField(default=1, help_text="Numero de habitacion")
    # Floor rooms
    floor = models.PositiveSmallIntegerField(default=1, help_text="Piso de la habitacion")
    # name rooms
    name = models.CharField(max_length=150, blank=False, null=False)
    # Description rooms
    description = models.CharField(max_length=500, blank=True, null=True)
    # Referencial Price rooms
    base_price = models.DecimalField(max_digits=6, decimal_places=2)
    # bill_to = models.CharField(max_length=30, blank=False, null=False)
