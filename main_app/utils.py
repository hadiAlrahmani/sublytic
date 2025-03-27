# main_app/utils.py

from django.core.mail import send_mail
from django.utils import timezone
from .models import Subscription

def send_renewal_reminders():
    # Get today's date and calculate the reminder range
    today = timezone.now().date()
    reminder_end_date = today + timezone.timedelta(days=7)  # Ends in 7 days

    # Get subscriptions with renewal dates within the next 7 days
    subscriptions = Subscription.objects.filter(
        renewal_date__gte=today,
        renewal_date__lte=reminder_end_date
    )

    # Send an email to each user with a renewal reminder
    for subscription in subscriptions:
        user = subscription.user
        subject = 'Upcoming Subscription Renewal Reminder'
        message = f'Hello {user.first_name},\n\n' \
                  f'Your subscription to {subscription.predefined_subscription.name} is set to renew on {subscription.renewal_date}.\n' \
                  f'You will be charged {subscription.predefined_subscription.price} BHD.\n\n' \
                  f'Thank you for using Sublytic!\n\n' \
                  f'Best regards,\nThe Sublytic Team'
        
        # Send the email to the user
        send_mail(
            subject,
            message,
            'no-reply@sublytic.com',  # From email
            [user.email],  # Recipient email
            fail_silently=False,
        )