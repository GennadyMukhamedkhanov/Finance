from celery import shared_task

# from django.core.mail import send_mail


@shared_task
def sending_letter_once_hour():
    print("Отправка письма!!!")
