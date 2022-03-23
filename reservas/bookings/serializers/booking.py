from datetime import datetime

# Django Rest Framework
from rest_framework import serializers

# Models
from reservas.bookings.models import PaymentMethod, State, Booking
from reservas.rooms.models import Room
from reservas.customers.models import Customer


class BookingSerializer(serializers.Serializer):
    check_in_date = serializers.DateField()
    check_out_date = serializers.DateField()
    # payment_method = serializers.PrimaryKeyRelatedField(source='paymentmethod.payment_method_id')
    # state = serializers.PrimaryKeyRelatedField(source='state.state_id')
    # room = serializers.PrimaryKeyRelatedField(source='room.room_id')

    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())

    def validate(self, data):
        server_date = datetime.now()
        """
        Check that start is before finish.
        """
        # Validar que las reservas no sean para fechas anteriores a la fecha del servidor
        if server_date.date() > data['check_in_date']:
            raise serializers.ValidationError({
                'check_in_date': 'No puede hacer registros para dias anteriores'
            })

        # Validar las fechas de llegada y salida
        if data['check_out_date'] < data['check_in_date']:
            raise serializers.ValidationError({
                'check_out_date': 'La fecha de salida no puede ser menor a la fecha de llegada'
            })

        # Validar disponibilidad de la habitacion en las fechas provistas por el cliente

        return data

    def create(self, validated_data):
        return Booking(**validated_data)
