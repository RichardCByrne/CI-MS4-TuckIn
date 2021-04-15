from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_profile, name='customer_profile'),
    path('customer_order_history/', views.customer_order_history, name='customer_order_history'),
]