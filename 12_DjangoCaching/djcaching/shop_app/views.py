from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.core.cache import cache
from .models import UserProfile, Order, Stocks, Offer, Shop, Product
from .forms import MyUserCreateForm


def main_page_view(request):
    return render(request, 'shop_app/index.html')


@login_required()
def personal_account_view(request):
    username = request.user.username
    stocks_cache_key = 'stocks:{}'.format(username)
    offers_cache_key = 'offers:{}'.format(username)
    stocks = cache.get(stocks_cache_key)
    if not stocks:
        stocks = Stocks.objects.all()
        cache.set(stocks_cache_key, stocks, 10)
    offers = cache.get(offers_cache_key)
    if not offers:
        offers = Offer.objects.all()
        cache.set(offers_cache_key, offers, 10)
    context = {
        'stocks': stocks,
        'offers': offers
    }
    return render(request, template_name='shop_app/account.html', context=context)


class UserLoginView(LoginView):
    next_page = reverse_lazy('shop:main')
    template_name = 'shop_app/login.html'


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('shop:main')


class UserCreate(CreateView):
    model = User
    form_class = MyUserCreateForm
    template_name = 'shop_app/user_create.html'
    success_url = reverse_lazy('shop:main')

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(self.request,
                            username=username,
                            password=password)
        login(request=self.request, user=user)
        UserProfile.objects.create(user=user)
        return response


class ShopsView(ListView):
    model = Shop
    template_name = 'shop_app/shops.html'
    context_object_name = 'shops'


class ShopCreateView(UserPassesTestMixin, CreateView):
    model = Shop
    template_name = 'shop_app/shop_create.html'
    success_url = reverse_lazy('shop:shops')
    fields = 'name', 'address'

    def test_func(self):
        return self.request.user.is_staff


class ProductsView(UserPassesTestMixin, ListView):
    model = Product
    template_name = 'shop_app/products.html'
    context_object_name = 'products'

    def test_func(self):
        return self.request.user.is_staff


class ProductCreateView(UserPassesTestMixin, CreateView):
    model = Product
    template_name = 'shop_app/product_create.html'
    success_url = reverse_lazy('shop:products')
    fields = 'name', 'description', 'price'

    def test_func(self):
        return self.request.user.is_staff
