from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_task_notification(email, subject, message):
    """Tarea asíncrona para enviar un correo de notificación al usuario"""
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )
