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
    title = models.CharField(max_length=100) #char field of max length 100 as title
    desc = models.TextField() #text field as descriptiong
    quad = models.CharField(max_length=100, choices=QUADRANT, default='Q4') #quadrant choices
    date = models.DateTimeField(default=timezone.now) #time of data creation

    def __str__(self): 
        return self.title #when asked for string return title


