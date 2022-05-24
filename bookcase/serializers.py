from rest_framework import serializers
from .models import BookItem
from core.serializers import UserSerializer

class BookItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookItem
        fields = ('id', 'owner', 'book', 'rack', 'stock')
        read_only_fields = ('id', 'owner', 'book', 'rack', 'stock')