from django.http import HttpResponseRedirect
from .models import Product, Order
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse


class ProductListView(ListView):
    queryset = Product.objects.filter(archived=False)
    context_object_name = 'products'
    template_name = 'shopapp/product_list.html'


class ProductDetailView(DetailView):
    queryset = Product.objects.filter(archived=False)
    context_object_name = 'product'
    template_name = 'shopapp/product_details.html'


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'discount']
    success_url = reverse_lazy('shopapp:products_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'discount']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('shopapp:product_details', kwargs={'pk': self.object.pk})


class ProductArchiveView(DeleteView):
    model = Product
    template_name_suffix = '_archived_form'

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)

    def get_success_url(self):
        return reverse('shopapp:products_list')


class OrderListView(ListView):
    queryset = Order.objects.select_related('user').prefetch_related('products')
    context_object_name = 'orders'
    template_name = 'shopapp/order_list.html'


class OrderDetailView(DetailView):
    queryset = Order.objects.select_related('user').prefetch_related('products')
    template_name = 'shopapp/order_details.html'
    context_object_name = 'order'


class OrderCreateView(CreateView):
    model = Order
    fields = 'delivery_address', 'promocode', 'user', 'products'

    def get_success_url(self):
        return reverse('shopapp:orders_list')


class OrderUpdateView(UpdateView):
    model = Order
    fields = 'delivery_address', 'promocode', 'user', 'products'
    template_name_suffix = '_update_form'
    context_object_name = 'order'

    def get_success_url(self):
        return reverse('shopapp:order_details', kwargs={'pk': self.object.pk})


class OrderDeleteView(DeleteView):
    model = Order
    template_name_suffix = '_delete_form'

    def get_success_url(self):
        return reverse('shopapp:orders_list')
