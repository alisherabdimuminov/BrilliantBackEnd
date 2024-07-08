from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True, null=False, blank=False, verbose_name="Foydalanuvchi nomi")
    first_name = models.CharField(max_length=50, verbose_name="Foydalanuvchi ismi")
    last_name = models.CharField(max_length=50, verbose_name="Foydalanuvchi familiyasi")

    objects = UserManager()
    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username
