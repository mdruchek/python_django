from django.views.generic import ListView, DetailView
from .models import Housing, News


class HousingListView(ListView):
    queryset = (Housing.objects
                .select_related('type')
                .prefetch_related('rooms')
                .all)
    context_object_name = 'housings'
    template_name = 'app_housing/housing_list.html'


class HousingDetailView(DetailView):
    model = Housing
    context_object_name = 'housing'


class NewsListView(ListView):
    model = News
    context_object_name = 'news'


class NewsDetailView(DetailView):
    model = News
    context_object_name = 'news'
