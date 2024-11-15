import datetime

from celery import shared_task
from django.utils import timezone

from config.settings import AUTH_USER_MODEL
from study.models import Course
from study.services import mail_sending


@shared_task
def send_update_mail(course_id):
    """Отправляет сообщение об обновлении курса всем его подписчикам."""
    course = Course.objects.get(pk=course_id)
    subscription_list = course.subscription.all()
    users = [subscription.user for subscription in subscription_list]
    subject = 'Обновление курса'
    message = f'Новые уроки в курсе "{course}"!'
    mail_sending(subject, message, users)


@shared_task
def ban_inactive():
    today = timezone.now().today().date()
    users = AUTH_USER_MODEL.objects.filter(last_login__lte=today - datetime.timedelta(days=30), is_active=True)
    for user in users:
        user.is_active = False
        user.save()
