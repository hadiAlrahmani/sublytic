from django.db import models
from django.contrib.auth.models import User

class PredefinedSubscription(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    renewal_period = models.CharField(max_length=255, help_text="e.g., Monthly, Yearly")
    image = models.ImageField(upload_to='subscriptions/', null=True, blank=True)

    def __str__(self):
        return self.name

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    predefined_subscription = models.ForeignKey(PredefinedSubscription, on_delete=models.SET_NULL, null=True)
    renewal_date = models.DateField()
    auto_renew = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.predefined_subscription.name} ({self.user.username})"
    
class SubscriptionPayment(models.Model):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    payment_date = models.DateField()

    def __str__(self):
        return f"Payment of {self.amount} for {self.subscription.predefined_subscription.name}"