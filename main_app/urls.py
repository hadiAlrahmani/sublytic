from django.urls import path
from .views import home, subscription_list, signup
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', home, name='home'),
    path('subscriptions/', subscription_list, name='subscription_list'),
    path('signup/', signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create-subscription/', views.create_subscription, name='create_subscription'),


]
