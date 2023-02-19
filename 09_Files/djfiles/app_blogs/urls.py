from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, upload_blog_csv


app_name = 'app_blogs'

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('create/', BlogCreateView.as_view(), name="create"),
    path('upload_file_csv/', upload_blog_csv, name="upload_file_csv"),
    path('<int:pk>', BlogDetailView.as_view(), name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
