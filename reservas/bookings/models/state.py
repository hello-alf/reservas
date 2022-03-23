"""State Model"""
from django.db import models
from reservas.utils.models import BookingAudit


class State (BookingAudit):
    state_id = models.CharField(primary_key=True, editable=False, max_length=3)
    # State Name
    name = models.CharField(max_length=20)
