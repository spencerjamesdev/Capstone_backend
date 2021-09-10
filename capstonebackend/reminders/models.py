from django.db import models
from django.db.models.fields import CharField, DateField, IntegerField

# Create your models here.
class Reminder(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    recurrence = models.IntegerField()
    day = models.DateField()
    user_id = models.IntegerField()
