from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Dog(models.Model):
    name = models.TextField()
    image = models.TextField()
    age = models.IntegerField()
    breed = models.TextField()
    human = models.TextField()
    zipcode = models.IntegerField()
    favGames = ArrayField(models.CharField(max_length=100))
