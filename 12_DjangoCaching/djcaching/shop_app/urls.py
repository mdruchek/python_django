from django.urls import path
from .views import main_page_view, personal_account_view

app_name = 'shop'

urlpatterns = [
    path('', main_page_view, name='main'),
    path('account', personal_account_view, name='account')
]
