from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.decorators import action
# Aqui irian importados el modelo de BookItem y su serializador
from rest_framework.response import Response
from  rest_framework import status

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset =  User.objects.all()

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]