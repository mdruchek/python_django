from django.urls import path
from .views import BlogListView, BlogDetailView


app_name = 'app_blogs'

urlpatterns = [
    path('', BlogListView.as_view(), name='blogs_list'),
    path('<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
]
