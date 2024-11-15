import smtplib

from config.settings import EMAIL_HOST_USER

from django.core.mail import send_mail


def mail_sending(subject, message, email):
    """Функция для отправки писем клиентам"""
    try:
        send_mail(subject=subject,
                  message=message,
                  from_email=EMAIL_HOST_USER,
                  recipient_list=[email, ],
                  )

    except smtplib.SMTPException as e:
        print(str(e))
