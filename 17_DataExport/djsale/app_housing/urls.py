from django.urls import path
from django.views.generic import TemplateView
from .views import HousingListView, HousingDetailView, NewsListView, NewsDetailView

urlpatterns = [
    path('contacts/', TemplateView.as_view(template_name='app_housing/contacts.html'), name='contacts'),
    path('about/', TemplateView.as_view(template_name='app_housing/about.html'), name='about'),
    path('housings/', HousingListView.as_view(), name='housing_list'),
    path('housings/<int:pk>/', HousingDetailView.as_view(), name='housing_detail'),
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
]
