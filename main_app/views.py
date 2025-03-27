from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Subscription, SubscriptionPayment, PredefinedSubscription  # Added PredefinedSubscription import
from .forms import SignUpForm, SubscriptionForm
from django.utils import timezone
import datetime
from django.core.mail import send_mail

def home(request):
    # Get today's date and calculate the reminder range
    today = timezone.now().date()
    reminder_start_date = today  # Reminder starts today
    reminder_end_date = today + timezone.timedelta(days=7)  # Ends in 7 days

    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Get the user's subscriptions that are within the reminder range
        upcoming_renewals = Subscription.objects.filter(
            user=request.user,
            renewal_date__gte=reminder_start_date,
            renewal_date__lte=reminder_end_date
        ).order_by('renewal_date')
    else:
        upcoming_renewals = None  # Set to None if the user is not logged in

    return render(request, 'main_app/home.html', {
        'upcoming_renewals': upcoming_renewals,  # Pass upcoming renewals to the template
        'today': today,
        'reminder_start_date': reminder_start_date,
        'reminder_end_date': reminder_end_date
    })

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
        predefined_subscription_id = request.POST.get('predefined_subscription')  # Get the subscription ID

        if not predefined_subscription_id:
            # Handle error if no subscription ID was selected (optional)
            return redirect('create_subscription')  # Redirect to the create page if no ID

        # Retrieve the predefined subscription object
        predefined_subscription = PredefinedSubscription.objects.get(id=predefined_subscription_id)

        renewal_date = request.POST.get('renewal_date')
        auto_renew = request.POST.get('auto_renew') == 'on'
        price = predefined_subscription.price  # Use predefined subscription's price

        # Create the subscription
        subscription = Subscription.objects.create(
            user=request.user,
            predefined_subscription=predefined_subscription,
            renewal_date=renewal_date,
            auto_renew=auto_renew,
            price=price
        )
        return redirect('subscription_list')  # Redirect to the subscription list after creation
    else:
        predefined_subscriptions = PredefinedSubscription.objects.all()
        return render(request, 'main_app/subscriptions/create_subscription.html', {'predefined_subscriptions': predefined_subscriptions})
    
# Edit Subscription View
@login_required
def edit_subscription(request, pk):
    subscription = Subscription.objects.get(pk=pk)
    if request.method == 'POST':
        form = SubscriptionForm(request.POST, request.FILES, instance=subscription)
        if form.is_valid():
            form.save()
            return redirect('subscription_list')
    else:
        form = SubscriptionForm(instance=subscription)

    return render(request, 'main_app/subscriptions/edit_subscription.html', {'form': form})

# Delete Subscription View
@login_required
def delete_subscription(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    if request.method == 'POST':
        subscription.delete()
        return redirect('subscription_list')
    return render(request, 'main_app/subscriptions/delete_subscription.html', {'subscription': subscription})

# View all subscriptions for the user
@login_required
def subscription_list(request):
    test_date = request.GET.get('test_date')

    if test_date:
        try:
            today = timezone.datetime.strptime(test_date, "%Y-%m-%d").date()
        except ValueError:
            today = timezone.now().date()
    else:
        today = timezone.now().date()

    reminder_start_date = today  # Reminder starts today
    reminder_end_date = today + timezone.timedelta(days=7)  # Ends in 7 days

    subscriptions = Subscription.objects.filter(user=request.user)
    return render(request, 'main_app/subscription_list.html', {
        'subscriptions': subscriptions,
        'today': today,
        'reminder_start_date': reminder_start_date,
        'reminder_end_date': reminder_end_date
    })

# View subscription payment history
@login_required
def subscription_history(request):
    payments = SubscriptionPayment.objects.filter(user=request.user).order_by('-date')
    return render(request, 'main_app/subscription_history.html', {
        'payments': payments
    })

