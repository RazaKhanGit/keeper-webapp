from django.db import models
from django.utils import timezone
# Create your models here.

QUADRANT = (
    ('Q1', 'important and urgent'),
    ('Q2', 'important and not urgent'),
    ('Q3', 'not important and urgent'),
    ('Q4', 'not important and not urgent')
)

class Note(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    quad = models.CharField(max_length=100, choices=QUADRANT, default='Q4')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self): 
        return self.title


