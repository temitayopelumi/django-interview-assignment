from rest_framework import serializers
from .models import Book
from authentication.models import User


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("title", "author")

    def create(self, validated_data):
        book = Book.objects.create(
            **validated_data
        )
        return book


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)
