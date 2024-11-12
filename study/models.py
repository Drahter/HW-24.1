from django.db import models

from config.settings import AUTH_USER_MODEL


class Course(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание курса')
    image = models.ImageField(upload_to='study/course_preview/', blank=True, null=True, verbose_name='Превью курса')
    owner = models.ForeignKey(AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                              verbose_name='Владелец')

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
    owner = models.ForeignKey(AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE,
                              verbose_name='Владелец')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Subscription(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', blank=True, null=True)
    is_active = models.BooleanField(default=False, verbose_name='Активность')

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

    def __str__(self):
        return f'Подписка {self.user} на курс {self.course}'
