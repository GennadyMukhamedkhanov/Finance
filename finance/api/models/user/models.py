from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")

    class Meta:
        db_table = "user"
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.first_name
