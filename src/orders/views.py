from django.shortcuts import render


def index(request):
    return render(request, 'orders/index.html')


def create_order(request):
    return render(request, 'orders/create.html')
