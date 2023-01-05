from django.urls import path
from .views import AdvertisementListView, AdvertisementDetailView

urlpatterns = [
    path('advertisements/', AdvertisementListView.as_view()),
    path('advertisements/<int:pk>', AdvertisementDetailView.as_view()),
]
