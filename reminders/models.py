from django.db import models
from subscriptions.models import Subscription
from django.contrib.auth.models import User

# Create your models here.

class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    renewal_date = models.DateTimeField() 
    auto_renew = models.BooleanField(default=True)
    message = models.TextField()  
    notification_time = models.DateTimeField()  
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('sent', 'Sent')], default='pending')  

    def __str__(self):
        return f"Reminder for {self.subscription.subscription_type.name} for {self.user.username}"