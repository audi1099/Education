from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    title = models.CharField(max_length=70, verbose_name="Название курса")
    duration = models.DurationField(verbose_name="Продолжительность")
    description = models.TextField(verbose_name="Описание курса")

    def __str__(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["id"]


class Topic(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название темы")
    discription = models.TextField(verbose_name="Описание темы")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"
        ordering = ["id"]




