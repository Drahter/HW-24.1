from celery import shared_task

from study.models import Course
from study.services import mail_sending


@shared_task
def send_update_mail(course_id):
    course = Course.objects.get(pk=course_id)
    subscription_list = course.subscription.all()
    users = [subscription.user for subscription in subscription_list]
    subject = 'Обновление курса'
    message = f'Новые уроки в курсе "{course}"!'
    mail_sending(subject, message, users)
