import os
from celery import Celery
from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from main_app.models import Subscription
from django.utils.timezone import now, timedelta


# Set the default Django settings module for Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sublytic.settings')

app = Celery('sublytic')

# Load settings from Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover tasks AFTER Django is ready
import django
django.setup()

app.autodiscover_tasks()

@app.task
def debug_task():
    print("Celery is working!")

@shared_task
def send_subscription_reminders():
    today = now().date()
    upcoming_subscriptions = Subscription.objects.filter(renewal_date=today + timedelta(days=2))

    for subscription in upcoming_subscriptions:
        user_email = subscription.user.email
        send_mail(
            subject="Subscription Renewal Reminder",
            message=f"Your {subscription.predefined_subscription.name} subscription will renew on {subscription.renewal_date}.",
            from_email="noreply@sublytic.com",
            recipient_list=[user_email],
        )

    return f"Sent {upcoming_subscriptions.count()} reminders"