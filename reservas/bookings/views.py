from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BookingAPIView(APIView):

    def post(self, request, format=None):
        data = {
            'status': 'ok',
            'message': 'Bien hecho'
        }
        return Response(data, status=status.HTTP_201_CREATED)
