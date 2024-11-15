from django.contrib.auth.models import AbstractUser
from django.db import models

from study.models import Course, Lesson


# Create your models here.
class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=150, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=150, blank=True, verbose_name='Фамилия')
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    avatar = models.ImageField(upload_to='users/users_avatars/', blank=True, null=True, verbose_name='Аватар')
    phone = models.CharField(max_length=35, verbose_name='Телефон', blank=True, null=True)
    country = models.CharField(max_length=35, blank=True, null=True, verbose_name='Страна')
    last_login = models.DateField(blank=True, null=True, verbose_name='Последний вход')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Payment(models.Model):
    PAYMENT_METHODS = (
        ('cash', 'Наличный'),
        ('non_cash', 'Безналичный')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,
                             verbose_name='Пользователь')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Оплата курса')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Оплата урока')
    price = models.PositiveIntegerField(default=0, verbose_name="Сумма оплаты")
    payment_method = models.CharField(max_length=15, choices=PAYMENT_METHODS, default='non_cash',
                                      verbose_name='Метод оплаты')

    session_id = models.CharField(max_length=255, blank=True, null=True, verbose_name='ID сессии',
                                  help_text='Укажите ID сессии')
    link = models.URLField(max_length=400, blank=True, null=True, verbose_name='Ссылка на оплату',
                           help_text='Укажите ссылку на оплату')

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'

    def __str__(self):
        return f'Оплата за {self.course or self.lesson} на {self.price} от {self.date}'
