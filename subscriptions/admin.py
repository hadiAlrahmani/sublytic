from django.contrib import admin
from .models import Subscription, SubscriptionType

# Register your models here.

admin.site.register(Subscription)
admin.site.register(SubscriptionType)