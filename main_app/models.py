from django.db import models

# Create your models here.
class Item(models.Model):
    description = models.CharField(max_length=100, unique=True)
    

    