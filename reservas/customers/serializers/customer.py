# Django Rest Framework
from rest_framework import serializers


class CustomerSerializer(serializers.Serializer):
    dni = serializers.CharField(max_length=30)
    first_name = serializers.CharField(max_length=30, required=False)
    last_name = serializers.CharField(max_length=150, required=False)
    bill_to = serializers.CharField(max_length=150)
