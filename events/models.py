from django.db import models

class Date(models.Model):
    date = models.DateField()

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.ForeignKey(Date, on_delete=models.CASCADE)
    description = models.TextField()

class Brochure(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    content = models.TextField()
