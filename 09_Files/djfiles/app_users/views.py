from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from .models import ProfileUser
from django.views.generic import (UpdateView,
                                  CreateView)
from .forms import RegistrationUserForm, UpdateUserForm
from .models import ProfileUser


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
        form = self.get_form()
        if form.is_valid():
            user = form.save()
            form.instace.avatar =ProfileUser(user=self.user, avatar=avatar)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        if form.is_valid():

        response = super().form_valid(form)
        avatar = self.request.FILES.get('avatar')
        if avatar:
            form.instace.avatar = ProfileUser.objects.create(user=self.request.user, avatar=avatar)
        username = form.cleaned_data.get('username')
        password = form.cleaned_date.get('password1')
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        return response


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
