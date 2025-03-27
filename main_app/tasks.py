from celery import shared_task
from .utils import send_renewal_reminders  # Import the send_renewal_reminders function

@shared_task
def send_subscription_renewal_reminders_task():
    send_renewal_reminders()