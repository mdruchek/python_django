from django.urls import path
from .views import (NewsCreateView,
                    NewsListView,
                    NewsDetailViews,
                    NewsUpdateView,
                    NewsArchivedView)

app_name = 'app_news'

urlpatterns = [
    path('', NewsListView.as_view(), name='list'),
    path('create/', NewsCreateView.as_view(), name='create'),
    path('<int:pk>/', NewsDetailViews.as_view(), name='details'),
    path('<int:pk>/update/', NewsUpdateView.as_view(), name='update'),
    path('<int:pk>/archived/', NewsArchivedView.as_view(), name='archived'),
]