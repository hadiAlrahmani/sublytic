from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Subscription(models.Model):
    name = models.CharField(max_length=100)
    renewal_date = models.DateField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Reminder(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    reminder_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title