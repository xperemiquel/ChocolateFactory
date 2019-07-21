from django.db import models

# Create your models here.

class OompaLoompa(models.Model):
    name = models.CharField(max_length=28)
    age = models.IntegerField()
    job = models.CharField(max_length=28)
    height = models.FloatField()
    weight = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name