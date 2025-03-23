from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Subscription
from .forms import SignUpForm
from .forms import SubscriptionForm

def home(request):
    return render(request, 'main_app/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('subscription_list')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def subscription_list(request):
    subscriptions = Subscription.objects.filter(user=request.user)
    return render(request, 'main_app/subscription_list.html', {'subscriptions': subscriptions})

@login_required
def create_subscription(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription = form.save(commit=False)
            subscription.user = request.user  # Assign the currently logged-in user to the subscription
            subscription.save()
            return redirect('subscription_list')  # Redirect to the list of subscriptions
    else:
        form = SubscriptionForm()

    return render(request, 'subscriptions/create_subscription.html', {'form': form})