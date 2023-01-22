from django.urls import path
from .views import shop_index, orders_list, products_list, product_create, order_create


app_name = 'shopapp'

urlpatterns = [
    path('', shop_index, name='shop-index'),
    path('orders/', orders_list, name='orders-list'),
    path('products/', products_list, name='products-list'),
    path('products/create/', product_create, name='product-create'),
    path('orders/create/', order_create, name='order-create'),
]
