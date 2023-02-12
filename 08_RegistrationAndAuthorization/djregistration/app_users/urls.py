from django.urls import path
from .views import (UserLoginView,
                    UserLogoutView,
                    register_view,
                    account_view,
                    UsersForAdminList)


app_name = 'app_users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('account/', account_view, name='account'),
    path('users_list/', UsersForAdminList.as_view(), name='users_list'),
]
