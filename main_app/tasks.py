from celery import shared_task
from django.core.mail import send_mail
from django.utils.timezone import now, timedelta
from .models import Subscription

@shared_task
def send_subscription_reminders():
    today = now().date()
    upcoming_subscriptions = Subscription.objects.filter(renewal_date=today + timedelta(days=2))

    # Log the upcoming subscriptions
    print(f"Upcoming subscriptions: {upcoming_subscriptions}")

    for subscription in upcoming_subscriptions:
        user_email = subscription.user.email
        send_mail(
            subject="Subscription Renewal Reminder",
            message=f"Your {subscription.predefined_subscription.name} subscription will renew on {subscription.renewal_date}.",
            from_email="noreply@sublytic.com",
            recipient_list=[user_email],
        )

    return f"Sent {upcoming_subscriptions.count()} reminders"