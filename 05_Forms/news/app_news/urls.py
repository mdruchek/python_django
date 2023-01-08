from django.urls import path
from app_news.views import NewsListView, NewsDetailView, NewsFormView, NewsEditFormView

urlpatterns = [
    path('news/', NewsListView.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('news/create/', NewsFormView.as_view(), name='news-create'),
    path('news/<int:news_id>/edit/', NewsEditFormView.as_view(), name='news-edit'),
]
