# Django Rest Framework
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response

# Models
from reservas.rooms.models import Room
from reservas.rooms.serializers import RoomSerializer


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def list_rooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

