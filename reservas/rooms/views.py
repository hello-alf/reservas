# Django Rest Framework
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response

# Models
from reservas.rooms.models import Room
from reservas.rooms.serializers import RoomSerializer


@api_view(['GET'])
@authentication_classes([]) # Add this
@permission_classes([]) # Maybe add this too
def list_rooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)


# @api_view(['POST'])
# def create_rooms(request):
#     serializer = CreateRoomSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     data = serializer.data
#     return Response(serializer.data)
