# Django Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from reservas.bookings.serializers import BookingSerializer


class BookingAPIView(APIView):

    def post(self, request, format=None):
        """Crete booking"""
        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        booking_done = serializer.save()
        data = {
            'status': 'ok',
            'body': booking_done
        }
        return Response(data, status=status.HTTP_201_CREATED)

