from django.shortcuts import render
from django


def main_page_view(request):
    return render(request, 'shop_app/index.html')


def personal_account_view(request):
    return render(request, 'shop_app/account.html')