from django.contrib.auth.models import AbstractUser
from django.db import models


class VideoServiceUser(AbstractUser):
    phone_number = models.CharField(max_length=12, unique=True, blank=False)
    avatar = models.FileField(upload_to='media', blank=True)

    def __str__(self):
        return self.username
