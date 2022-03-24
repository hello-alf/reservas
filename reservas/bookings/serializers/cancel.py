# Django Rest Framework
from rest_framework import serializers

# Models
from reservas.customers.models import Customer
from reservas.bookings.models import Booking, State


class CancelBookingSerializer(serializers.Serializer):
    booking = serializers.CharField()
    customer = serializers.CharField()

    def validate(self, data):
        # Validamos si el cliente existe
        try:
            data['customer'] = Customer.objects.get(dni=data['customer'])
        except Customer.DoesNotExist:
            raise serializers.ValidationError({
                'customer': 'El cliente no existe'
            })

        # Filtramos las reservas pagadas o pendientes
        try:
            Booking.objects.get(booking_id=data['booking'],
                                customer=data['customer'],
                                state_id__in=['PEN', 'PAG'])
        except Booking.DoesNotExist:
            raise serializers.ValidationError({
                'customer': 'El cliente no tiene ninguna reserva'
            })
        return data

    def update(self, instance):
        # Seteamos el estado eliminado a la reserva obtenida
        instance.state_id = 'ELI'
        instance.save()
        return instance
