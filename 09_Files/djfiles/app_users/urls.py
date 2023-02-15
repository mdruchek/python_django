from django.urls import path
from .views import (UsersLoginView,
                    UserLogoutView,
                    UserCreateView,
                    user_update_view,
                    user_account_view)


app_name = 'app_users'

urlpatterns = [
    path('login/', UsersLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('create/', UserCreateView.as_view(), name='create'),
    path('account/', user_account_view, name='account'),
    path('update/', user_update_view, name='update'),
]
