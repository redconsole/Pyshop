from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    price = models.IntegerField
    url = models.CharField(max_length=2023)

