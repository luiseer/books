from book.models import Book
from rest_framework import serializers
from .models import BookItem
from core.serializers import UserSerializer
from book.serializers import BookSerializer


class BookItemSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    book = BookSerializer()
    class Meta:
        model = BookItem
        fields = ('__all__')
        depth = 1