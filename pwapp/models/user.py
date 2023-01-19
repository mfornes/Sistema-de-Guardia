
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    email = models.EmailField(unique=True)
    description = models.TextField("Description", max_length=600, default='', blank=True)

    def __str__(self):
        return self.username