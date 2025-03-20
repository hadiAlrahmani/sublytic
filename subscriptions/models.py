from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class SubscriptionType(models.Model):
    name = models.CharField(max_length=255, unique=True) 
    category = models.CharField(max_length=50) 
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    billing_cycle = models.CharField(max_length=50) 

    def __str__(self):
        return self.name

class Subscription(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  
    subscription_type = models.ForeignKey(SubscriptionType, on_delete=models.CASCADE)  
    renewal_date = models.DateTimeField()  
    auto_renew = models.BooleanField(default=True) 
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active') 

    def __str__(self):
        return f"{self.subscription_type.name} - {self.user.username}"