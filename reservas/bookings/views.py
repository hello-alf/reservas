# Django Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers

# Django
from django.http import HttpResponse

# Models
from reservas.bookings.models import Booking

# Custom Serializers
from reservas.bookings.serializers import BookingSerializer, CancelBookingSerializer


class BookingAPIView(APIView):
    # Definimos el acceso publico del servicio
    authentication_classes = ([])
    permission_classes = ([])

    def post(self, request, format=None):
        """Create booking"""
        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, format=None):
        try:
            booking = Booking.objects.get(pk=request.data['booking'])
        except Booking.DoesNotExist:
            return HttpResponse(status=404)
        serializer = CancelBookingSerializer(booking, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": "Reserva eliminada correctamente"}, status=status.HTTP_200_OK)

