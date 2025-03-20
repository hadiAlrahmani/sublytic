from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('subscriptions/', views.subscription_list, name='subscription_list'),
    path('reminders/', views.reminder_list, name='reminder_list'),
]
