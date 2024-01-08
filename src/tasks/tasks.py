import smtplib
from email.message import EmailMessage

from celery import Celery

from src.config import SMTP_PASSWORD, SMTP_USER, REDIS_HOST, REDIS_PORT, SMTP_HOST, SMTP_PORT, TO_SEND_EMAIL_TEST

celery = Celery('tasks', broker=f'redis://{REDIS_HOST}:{REDIS_PORT}')


def get_email_template_dashboard(username: str):
    email = EmailMessage()
    email['Subject'] = 'Отчет за месяц'
    email['From'] = SMTP_USER
    email['To'] = TO_SEND_EMAIL_TEST

    email.set_content(
        '<div>'
        f'<h1 style="color: red;">Здравствуйте, {username}, вот ваш отчет за месяц.</h1>'
        '<img src="https://www.kadrof.ru/sites/default/files/illustrations/seo_otchet.jpg" width="600">'
        '</div>',
        subtype='html'
    )
    return email


@celery.task
def send_email_report_dashboard(username: str):
    email = get_email_template_dashboard(username)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)
