from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


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


class Payments(models.Model):
    PAYMENT_METHODS = [
        ('cash', 'Наличные'),
        ('transfer', 'Перевод на счет'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS)


    def __str__(self):
        return f'{self.user} - {self.course}|{self.lesson}, {self.amount} {self.payment_date}'

    class Meta:
        verbose_name = "Платёж"
        verbose_name_plural = "Платежи"
