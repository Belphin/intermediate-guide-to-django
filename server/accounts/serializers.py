from rest_framework import serializers
from .constants import UserRoleChoice


class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=1, max_length=64, write_only=True)
    username = serializers.CharField(max_length=64, write_only=True)
    password = serializers.CharField(min_length=8, max_length=64, write_only=True)
    role = serializers.ChoiceField(choices=UserRoleChoice.choices)

    success = serializers.BooleanField(read_only=True)
    error = serializers.CharField(read_only=True)