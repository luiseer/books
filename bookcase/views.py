from django.shortcuts import render
from .models import BookItem
from .serializers import BookItemSerializer
from rest_framework import viewsets, status
from rest_framework.permissions import  IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.decorators import action
from bookcase.models import BookItem
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



class BookItemViewSet(viewsets.ModelViewSet):
    queryset = BookItem.objects.all()
    serializer_class =  BookItemSerializer
    
    # Filter inside nested serializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['book__title','book__author','book__book_id','book__genre','book__date_of_publication']
    search_fields = ['book__title','book__author','book__book_id','book__genre','book__date_of_publication']
    
    
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class BookItemLendViewSet(viewsets.ModelViewSet):
    
    queryset = BookItem.objects.all()
    serializer_class = BookItemSerializer
    
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'update':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
    
    @action(detail=True)
    def lend_book(self, request, pk=None):
        user = request.user
        bookitem = BookItem.objects.get(id=pk)
        if bookitem.current_owner == None:
            bookitem.current_owner = request.user
            user.rented_books += 1
            if user.rented_books > 3:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            bookitem.save()
            user.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True)
    def return_book(self, request, pk=None):
        user = request.user
        bookitem = BookItem.objects.get(id=pk)
        if bookitem.current_owner == request.user:
            bookitem.current_owner = None
            user.rented_books -= 1
            bookitem.save()
            user.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)