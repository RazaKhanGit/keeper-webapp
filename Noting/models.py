from django.db import models
from django.utils import timezone
# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    date = models.DateTimeField(default=timezone.now)

  
    def __str__(self): 
        return self.title