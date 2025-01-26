from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    """Форма на основе модели Order для создания заказа."""

    class Meta:
        model = Order
        exclude = ('total_price',)
