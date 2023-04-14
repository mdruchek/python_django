from django.contrib import admin
from .models import Offer, Stocks


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = 'product', 'discount'


@admin.register(Stocks)
class StocksAdmin(admin.ModelAdmin):
    list_display = 'name', 'description', 'promo_code', 'discount'
