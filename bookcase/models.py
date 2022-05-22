# from unicodedata import name
from django.db import models
from book.models import Book
import uuid

# Create your models here.


    
    

class Rack(models.Model):
    rack_id = models.UUIDField(default=uuid.uuid4())
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, blank=True)
    def __str__(self):
        return self.name
    

class RackItem(models.Model):
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    