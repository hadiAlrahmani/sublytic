from django.contrib import admin
from .models import Subscription, SubscriptionPayment, PredefinedSubscription

@admin.register(PredefinedSubscription)
class PredefinedSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'renewal_period', 'description', 'image')

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'predefined_subscription', 'renewal_date', 'auto_renew', 'price')
    search_fields = ('user__username', 'predefined_subscription__name')

@admin.register(SubscriptionPayment)
class SubscriptionPaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'subscription', 'amount', 'payment_date')
    search_fields = ('subscription__user__username', 'subscription__predefined_subscription__name')