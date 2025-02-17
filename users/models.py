from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Почта пользователя")
    phone = models.CharField(max_length=45, blank=True, null=True, verbose_name="Телефон пользователя")
    tg_nick = models.CharField(max_length=15, blank=True, null=True, verbose_name="Телеграмм ник")
    city = models.CharField(max_length=20, verbose_name="Город")
    avatar = models.ImageField(upload_to="users/avatars", blank=True, null=True, verbose_name="Аватар")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.username} {self.email}'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


