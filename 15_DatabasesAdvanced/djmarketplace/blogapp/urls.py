from django.urls import path
from .views import articles_list_view

urlpatterns = [
    path('', articles_list_view, name='blogs'),
]