from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}  # Optional; used to further customize a declared field

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)  # ** indicates that all keyword args will be given as dict
        return user
