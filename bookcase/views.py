from django.shortcuts import render
from .models import BookItem
from .serializers import BookItemSerializer
from rest_framework.permissions import  IsAdminUser, IsAuthenticated
from rest_framework import viewsets
class BookItemViewSet(viewsets.ModelViewSet):
    queryset = BookItem.objects.all()
    serializer_class = BookItemSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
