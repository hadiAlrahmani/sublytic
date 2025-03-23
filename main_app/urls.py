from django.urls import path
from .views import home, subscription_list, signup
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('subscriptions/', subscription_list, name='subscription_list'),
    path('signup/', signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('subscriptions/create/', views.create_subscription, name='create_subscription'),
    path('subscriptions/edit/<int:pk>/', views.edit_subscription, name='edit_subscription'),  
    path('subscriptions/delete/<int:pk>/', views.delete_subscription, name='delete_subscription'), 
]