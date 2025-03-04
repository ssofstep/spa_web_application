from django.db import models

from config.settings import AUTH_USER_MODEL


class Course(models.Model):
    title = models.CharField(verbose_name="Название курса", max_length=100)
    image = models.ImageField(verbose_name="Картинка", blank=True)
    description = models.TextField(verbose_name="Описание курса", null=True, blank=True)
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец курса", blank=True,
                              null=True)

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(verbose_name="Название урока", max_length=100)
    image = models.ImageField(verbose_name="Картинка", blank=True)
    description = models.TextField(verbose_name="Описание урока", null=True, blank=True)
    link = models.CharField(verbose_name="Ссылка на видео", max_length=200)
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец урока", blank=True,
                              null=True)

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Subscription(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь", blank=True,
                              null=True),
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Подписка на курс"),
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Подписка на урок"),
    sign_of_subscription = models.BooleanField(verbose_name="Признак подписки")

    def __str__(self):
        return f'{self.user} {self.course}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'