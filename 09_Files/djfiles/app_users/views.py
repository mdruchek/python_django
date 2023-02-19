from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import (UpdateView,
                                  CreateView)
from .forms import RegistrationUserForm, UpdateUserForm


class UsersLoginView(LoginView):
    template_name = 'app_users/login.html'
    next_page = reverse_lazy('app_blogs:list')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('app_blogs:list')


class UserCreateView(CreateView):
    model = User
    form_class = RegistrationUserForm
    template_name = 'app_users/create.html'
    success_url = reverse_lazy('app_blogs:list')

    def post(self, request, *args, **kwargs):
        form =


@login_required(login_url=reverse_lazy('app_users:login'))
def user_account_view(request):
    return render(request, 'app_users/account.html')


@login_required(login_url=reverse_lazy('app_users:login'))
def user_update_view(request):
    user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            user.save()
    else:
        form = UpdateUserForm(instance=user)
    context = {
        'form': form
    }
    return render(request, 'app_users/update.html', context=context)
