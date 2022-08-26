import math
import random

from django.contrib.auth import authenticate, user_logged_in
from django.db.models import fields
from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)

from .models import User


class RegisterMemberSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=128, min_length=8, write_only=True)
    password2 = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "password1", "password2")
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password1"],
        )
        
        return user

    def validate(self, attrs):
        if attrs.get("password1") != attrs.get("password2"):
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        try:
            user = User.objects.get(username=attrs.get("username"))
            if user:
                raise serializers.ValidationError({"username": "A user with this username exists"})
        except User.DoesNotExist:
            return attrs

class RegisterLibrarianSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=128, min_length=8, write_only=True)
    password2 = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "password1", "password2")
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password1"],
            group = "LIBRARIAN"
        )
        
        return user

    def validate(self, attrs):

        if attrs.get("password1") != attrs.get("password2"):
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        try:
            user = User.objects.get(username=attrs.get("username"))
            if user:
                raise serializers.ValidationError({"username": "A user with this username exists"})
        except User.DoesNotExist:
            return attrs