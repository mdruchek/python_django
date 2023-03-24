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
    # success_url = reverse_lazy('app_blogs:list')

    def post(self, request, *args, **kwargs):
        form = RegistrationUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            avatar = form.cleaned_data.get('avatar')
            if avatar:
                ProfileUser.objects.create(user=user, avatar=avatar)
            return HttpResponseRedirect(reverse('app_blogs:list'))


@login_required(login_url=reverse_lazy('app_users:login'))
def user_account_view(request):
    return render(request, 'app_users/account.html')


@login_required(login_url=reverse_lazy('app_users:login'))
def user_update_view(request):
    user = User.objects.get(username=request.user.username)
    profile_user = ProfileUser.objects.get(user=user)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user.save()
            if form.cleaned_data['avatar']:
                profile_user.avatar = form.cleaned_data['avatar']
            else:
                profile_user.avatar = ''
            profile_user.save()
            return redirect(reverse('app_users:account'))
    else:
        form = UpdateUserForm(instance=user)
    context = {
        'form': form
    }
    return render(request, 'app_users/update.html', context=context)
