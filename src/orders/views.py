from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse

from .models import Order
from .forms import OrderForm


def index(request):
    """Функция представления главной страницы."""
    return render(request, 'orders/index.html')


# def create_order(request):
#     return render(request, 'orders/create.html')

class OrderCreateView(CreateView):
    """Класс представления создания заказа."""

    model = Order
    form_class = OrderForm
    template_name = 'orders/create.html'

    def get_success_url(self):
        return reverse('orders:index')

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)