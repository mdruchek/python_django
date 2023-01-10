from django.shortcuts import render
from django.http import HttpRequest


def shop_index(request: HttpRequest):
    return render(request, 'shopapp/shop-index.html')
