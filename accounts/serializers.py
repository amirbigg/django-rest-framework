from rest_framework import serializers


class UserRegisterSerializer(serializers.Serializer):
	username = serializers.CharField(required=True)
	email = serializers.EmailField(required=True)
	password = serializers.CharField(required=True, write_only=True)
