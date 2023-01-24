from django.urls import path

from .views import (ProductListView,
                    ProductCreateView,
                    ProductUpdateView,
                    ProductDetailView,
                    ProductArchiveView,
                    OrderListView,
                    OrderDetailView,
                    OrderCreateView,
                    OrderUpdateView,
                    OrderDeleteView)

app_name = "shopapp"

urlpatterns = [
    path("products/", ProductListView.as_view(), name="products_list"),
    path("products/create", ProductCreateView.as_view(), name="product_create"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_details"),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("products/<int:pk>/archived/", ProductArchiveView.as_view(), name="product_archived"),
    path("orders/", OrderListView.as_view(), name="orders_list"),
    path("orders/create/", OrderCreateView.as_view(), name="order_create"),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order_details"),
    path("orders/<int:pk>/update", OrderUpdateView.as_view(), name="order_update"),
    path("order/<int:pk>/delete/", OrderDeleteView.as_view(), name="order_delete"),
]
