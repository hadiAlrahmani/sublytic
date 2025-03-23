from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Subscription, PredefinedSubscription
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

# Create Subscription View
@login_required 
def create_subscription(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription = form.save(commit=False)  # Do not save yet
            subscription.user = request.user
            subscription.save()  # Now save it
            return redirect('subscription_list')
    else:
        form = SubscriptionForm()
    return render(request, 'subscriptions/create_subscription.html', {'form': form})

# Edit Subscription View
def edit_subscription(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    if request.method == 'POST':
        form = SubscriptionForm(request.POST, instance=subscription)
        if form.is_valid():
            form.save()
        return redirect('subscription_list')
    else:
        form = SubscriptionForm(instance=subscription)
        return render(request, 'main_app/subscriptions/edit_subscription.html', {'form': form, 'subscription': subscription})
    
# Delete Subscription View
def delete_subscription(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    if request.method == 'POST':
        subscription.delete()
        return redirect('subscription_list')
    return render(request, 'main_app/subscriptions/delete_subscription.html', {'subscription': subscription})

# View all subscriptions for the user
def subscription_list(request):
    subscriptions = Subscription.objects.filter(user=request.user)
    return render(request, 'main_app/subscription_list.html', {'subscriptions': subscriptions})