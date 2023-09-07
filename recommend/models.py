from typing import Any
from django.db import models

# Create your models here.
class Movie(models.Model):
    id = models.BigAutoField(name="id", primary_key=True)
    title = models.CharField(name="name", max_length=200)
    year = models.IntegerField(name="year", blank=True, null=True)
    genres = models.CharField(name="genres", max_length=100)
