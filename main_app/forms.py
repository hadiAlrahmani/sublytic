from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Subscription, PredefinedSubscription

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class SubscriptionForm(forms.ModelForm):
    predefined_subscription = forms.ModelChoiceField(queryset=PredefinedSubscription.objects.all(), empty_label="Choose Subscription")
    renewal_date = forms.DateField()
    auto_renew = forms.BooleanField(initial=True)
    
    class Meta:
        model = Subscription
        fields = ['predefined_subscription', 'renewal_date', 'auto_renew']