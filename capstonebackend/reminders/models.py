from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField, DateField, IntegerField

# Create your models here.
class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    recurrence = models.IntegerField()
    day = models.DateField()
    is_completed = models.BooleanField(default=False)
    
