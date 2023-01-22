from django.shortcuts import render, reverse, redirect
from django.http import HttpRequest
from .models import Product, Order
from .forms import ProductForm, OrderForm


def shop_index(request: HttpRequest):
    return render(request, 'shopapp/shop-index.html')


def products_list(request: HttpRequest):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'shopapp/products-list.html', context=context)


def orders_list(request: HttpRequest):
    context = {
        'orders': Order.objects.select_related('user').prefetch_related('products').all(),
    }
    return render(request, 'shopapp/orders-list.html', context=context)


def product_create(request: HttpRequest):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            url = reverse('shopapp:products-list')
            return redirect(url)
    else:
        form = ProductForm()
    context = {
        'form': form,
    }
    return render(request, 'shopapp/product-create.html', context=context)


def order_create(request:HttpRequest):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            url = reverse('shopapp:orders-list')
            return redirect(url)
    else:
        form = OrderForm()
    context = {
        'form': form
    }
    return render(request, 'shopapp/order-create.html', context=context)

