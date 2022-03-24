from datetime import datetime, date

# Django Rest Framework
from rest_framework import serializers

# Models
from reservas.bookings.models import PaymentMethod, State, Booking
from reservas.rooms.models import Room
from reservas.customers.serializers.customer import CustomerSerializer
from reservas.customers.models import Customer


class BookingSerializer(serializers.Serializer):
    check_in_date = serializers.DateField()
    check_out_date = serializers.DateField()
    payment_method = serializers.PrimaryKeyRelatedField(queryset=PaymentMethod.objects.all(),
                                                        required=False,
                                                        allow_null=True)
    state = serializers.PrimaryKeyRelatedField(queryset=State.objects.all(),
                                               required=False,
                                               allow_null=True)
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())
    # amount = serializers.DecimalField(max_digits=6, decimal_places=2)
    customer = CustomerSerializer(required=True)

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
        is_available = Booking.objects.filter(room=data['room'],
                                              check_in_date__lte=data['check_in_date'],
                                              check_out_date__gte=data['check_out_date']).count()

        if is_available > 0:
            raise serializers.ValidationError({
                'room': 'La habitacion se encuentra ocupada en la fecha seleccionada'
            })

        # Calculamos los dias de estadia
        delta = data['check_out_date'] - data['check_in_date']
        number_of_nights = delta.days + 1

        # Calculamos el costo de hospedaje
        self.context['amount'] = number_of_nights * data['room'].base_price

        # Verificamos el estado enviado que por defecto es PENDIENTE
        if 'state' not in data:
            data['state'] = State.objects.get(state_id='PEN')
        else:
            # En caso de ser una reserva pagada con anticipacion
            if data['state'].state_id == 'PAG':
                # Verificamos el metodo de pago
                if 'payment_method' not in data:
                    raise serializers.ValidationError({
                        'payment_method': 'Debe seleccionar un metodo de pago'
                    })

        return data

    def create(self, validated_data):
        customer_data = validated_data.pop('customer')
        # Creamos al cliente nuevo si no existiese
        obj, created = Customer.objects.get_or_create(
            **customer_data
        )
        # Creamos la reserva
        booking_instance = Booking.objects.create(customer=obj, amount=self.context['amount'], **validated_data)
        return booking_instance
