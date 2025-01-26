from django.urls import path

from .views import index, OrderCreateView

app_name = 'order'

urlpatterns = [
    path('', index, name='index'),
    path('orders/create/', OrderCreateView.as_view(), name='create_order')
]
