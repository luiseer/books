from django.db import models
from book.models import Book
from core.models import User
import uuid

# Create your models here.

class Rack(models.Model):
    rack_id = models.UUIDField(default=uuid.uuid4())
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, blank=True)
    def __str__(self):
        return self.name
    

class BookItem(models.Model):
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    stock = models.IntegerField(max_length=1, default=5)    
    def __str__(self) -> str:
        return f"{self.book} | {self.rack} | {self.id}"