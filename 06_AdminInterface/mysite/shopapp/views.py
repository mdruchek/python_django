from django.shortcuts import render
from django.http import HttpRequest
from .models import Product, Order


def shop_index(request: HttpRequest):
    return render(request, 'shopapp/shop-index.html')


def products_list(request: HttpRequest):
    context = {
        'products': Product.objects.prefetch_related('user').all(),
    }
    return render(request, 'shopapp/products-list.html', context=context)


def orders_list(request: HttpRequest):
    context = {
        'orders': Order.objects.select_related('user').prefetch_related('products').all(),
    }
    return render(request, 'shopapp/orders-list.html', context=context)
