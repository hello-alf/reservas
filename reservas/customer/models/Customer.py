import uuid

"""Customer Model"""
from django.db import models
from reservas.utils.models import BookingAudit


class Customer (BookingAudit):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    dni = models.CharField(max_length=30, blank=True, null=True)
    bill_to = models.CharField(max_length=30, blank=False, null=False)
