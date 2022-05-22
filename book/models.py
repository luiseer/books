from django.db import models
from core.models import User
import uuid
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    book_id = models.UUIDField(default=uuid.uuid4())
    genre = models.CharField(max_length=100)
    des = models.TextField(max_length=1000)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
