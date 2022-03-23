from rest_framework import serializers


class RoomSerializer(serializers.Serializer):
    room_id = serializers.IntegerField()
    number = serializers.IntegerField()
    floor = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    base_price = serializers.DecimalField(max_digits=6, decimal_places=2)


# class CreateRoomSerializer(serializers.Serializer):
#     number = serializers.IntegerField(max_value=9999, min_value=1)
#     floor = serializers.IntegerField(max_value=9999, min_value=1)
#     name = serializers.CharField(max_length=150)
#     description = serializers.CharField(max_length=500, allow_blank=True, allow_null=True)
#     base_price = serializers.DecimalField(max_digits=6, decimal_places=2)
