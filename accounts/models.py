from django.contrib.auth.models import AbstractUser
from django.db import models
from django.apps import apps

class CustomUser(AbstractUser):
    description = models.CharField(max_length=511)
    image = models.ImageField(blank=True, upload_to='img/%Y/%m/%d/')
    
    def __str__(self):
        return self.username