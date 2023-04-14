from django.urls import path
from .views import (main_page_view,
                    personal_account_view,
                    UserLoginView,
                    UserLogoutView,
                    UserCreate,
                    ShopsView,
                    ShopCreateView,
                    ProductsView,
                    ProductCreateView)

app_name = 'shop'

urlpatterns = [
    path('', main_page_view, name='main'),
    path('products/', ProductsView.as_view(), name='products'),
    path('products/product-create/', ProductCreateView.as_view(), name='product_create'),
    path('shops/', ShopsView.as_view(), name='shops'),
    path('shops/shop-create/', ShopCreateView.as_view(), name='shop_create'),
    path('account/', personal_account_view, name='account'),
    path('account/login/', UserLoginView.as_view(), name='login'),
    path('account/logout/', UserLogoutView.as_view(), name='logout'),
    path('account/create/', UserCreate.as_view(), name='user_create'),
]
