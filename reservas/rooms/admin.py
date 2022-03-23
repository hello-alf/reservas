# Django
from django.contrib import admin

# Custom
from reservas.rooms.models import Room


class RoomAdmin(admin.ModelAdmin):
    """Device model admin"""
    list_display = ('name', 'description', 'number', 'floor', 'base_price')


admin.site.register(Room, RoomAdmin)
