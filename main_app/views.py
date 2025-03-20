from django.shortcuts import render
from .models import Subscription, Reminder
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def subscription_list(request):
    subscriptions = Subscription.objects.all()
    return render(request, 'subscription_list.html', {'subscriptions': subscriptions})

def reminder_list(request):
    reminders = Reminder.objects.all()
    return render(request, 'reminder_list.html', {'reminders': reminders})