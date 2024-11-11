from django.db import models

from users.models import User


class Course(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание курса')
    image = models.ImageField(upload_to='study/course_preview/', blank=True, null=True, verbose_name='Превью курса')
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Владелец')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание урока')
    image = models.ImageField(upload_to='study/lesson_preview/', blank=True, null=True, verbose_name='Превью урока')
    course = models.ForeignKey(Course, verbose_name='Курс', on_delete=models.CASCADE, related_name='lesson_set')
    url = models.URLField(blank=True, null=True, verbose_name='ссылка')
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Владелец')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
