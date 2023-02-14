from django.urls import path
from .views import (AuthUsersView,
                    registration_view)


app_name = 'app_users'

urlpatterns = [
    path('login/', AuthUsersView.as_view(), name='login'),
    path('registration/', registration_view, name='registration'),
]