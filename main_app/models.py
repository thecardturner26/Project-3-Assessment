from django.db import models
from django.urls import reverse
# Create your models here.


class Item(models.Model):
    description = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index', kwargs={'list_id': self.id})

    