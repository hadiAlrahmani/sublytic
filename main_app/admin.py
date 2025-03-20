from django.contrib import admin
from .models import Subscription, Reminder

# Register your models here.

admin.site.register(Subscription)
admin.site.register(Reminder)
