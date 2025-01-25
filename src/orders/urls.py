from django.urls import path

from .views import index, create_order

urlpatterns = [
    path('', index),
    path('orders/create/', create_order)
]
