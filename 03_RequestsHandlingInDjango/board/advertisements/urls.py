from django.urls import path
from . import views

urlpatterns = [
    path('', views.advertisement_list, name='advertisement_list'),
    path('advertisements/', views.Advertisements.as_view()),
    path('contacts/', views.Contacts.as_view())
]
