"""Customer Model"""

import uuid

from django.db import models
from reservas.utils.models import BookingAudit


class Customer (BookingAudit):
    customer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Customer's name
    first_name = models.CharField(max_length=30, blank=False, null=False)
    # Customer's lastname
    last_name = models.CharField(max_length=150, blank=False, null=False)
    # Customer's identity AKA ci
    dni = models.CharField(max_length=30, blank=True, null=True)
    # Customer's bill to data for invoice
    bill_to = models.CharField(max_length=30, blank=False, null=False)
    # Customer's foreign state
    is_foreign = models.BooleanField(default=False)
