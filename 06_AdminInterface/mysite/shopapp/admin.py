from django.contrib import admin
from .models import Product, Order
from django.db.models import Queryset
from django.http import HttpRequest


class OrderInline(admin.TabularInline):
    model = Product.orders.through


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    actions = ['mark_archived',]

    fieldsets = (
        (None, {
            'fields': ('name', 'description_short'),
            'classes': ('wide',)

        }),
        ('Price', {
            'fields': ('price', 'discount'),
            'classes': ('wide',)
        }),
        ('Other', {
            'fields': ('arhived', 'created_at'),
            'classes': ('collapse',)
        })
    )

    inlines = [
        OrderInline
    ]
    # list_display = 'pk', 'name', 'description_short', 'price', 'discount', 'arhived'
    list_display_links = 'pk', 'name'
    ordering = '-price',
    search_fields = 'name', 'description', 'discount'

    def descriptions_short(self, obj: Product) -> str:
        if len(obj.description) > 30:
            return '{desc}...'.format(desc=self.description[:30])
        return obj.description

    @admin.actions(descriptions='Перевести в архив')
    def mark_archived(self, request: HttpRequest, queryset: Queryset):
        queryset.update(arhived=True)


class ProductInline(admin.TabularInline):
    model = Order.products.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]
    list_display = 'pk', 'delivery_address', 'promocode', 'user_verbose'
    list_display_links = 'pk', 'name'
    ordering = '-pk',
    search_fields = 'user', 'delivery_address'

    def get_queryset(self, request: HttpRequest):
        return Order.objects.select_related('user').prefetch_related('products')

    def user_verbose(self, obj: Order) -> str:
        return obj.user.firstname
