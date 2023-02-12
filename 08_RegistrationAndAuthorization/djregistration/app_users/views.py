from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView
from .forms import UserRegisterForm
from .models import Profile
from app_news.models import NewsModel


class UserLoginView(LoginView):
    template_name = 'app_users/login.html'
    next_page = reverse_lazy('main')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('main')


def register_view(request: HttpRequest):
    users_group, created_user_group = Group.objects.get_or_create(name='users')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.groups.add(users_group)
            telephone = form.cleaned_data.get('telephone')
            city = form.cleaned_data.get('city')
            Profile.objects.create(
                user=user,
                telephone=telephone,
                city=city
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'app_users/register.html', context=context)


def account_view(request):
    return render(request, 'app_users/account.html')


class UsersForAdminList(PermissionRequiredMixin, ListView):
    permission_required = 'auth.can_verify_users'
    raise_exception = False
    login_url = reverse_lazy('app_users:login')
    queryset = User.objects.prefetch_related('groups').filter(is_superuser=False)
    context_object_name = 'users_list'
    template_name = 'app_users/users_list.html'
    users_group, created_user_group = Group.objects.get_or_create(name='users')
    moderator_group, created_moderator_group = Group.objects.get_or_create(name='moderators')
    if created_moderator_group:
        content_type_user = ContentType.objects.get_for_model(User)
        content_type_news = ContentType.objects.get_for_model(NewsModel)
        permission_verify_users = Permission.objects.create(
            codename='can_verify_users',
            name='Может верифицировать пользователей',
            content_type=content_type_user
        )
        permission_publish = Permission.objects.get(
            codename='can_publish',
            content_type=content_type_news
        )
        permission_delete_news = Permission.objects.get(
            codename='delete_newsmodel',
            content_type=content_type_news
        )
        moderator_group.permissions.set([permission_verify_users, permission_publish, permission_delete_news])

    verified_users_group, created_verifiedusers_group = Group.objects.get_or_create(name='verifiedusers')
    if created_verifiedusers_group:
        content_type = ContentType.objects.get_for_model(NewsModel)
        permission_add = Permission.objects.get(
            codename='add_newsmodel',
            content_type=content_type
        )
        permission_change = Permission.objects.get(
            code_name='change_newsmodel',
            content_type=content_type
        )
        verified_users_group.permissions.set([permission_add, permission_change])

    def post(self, request):
        queryset = User.objects.prefetch_related('groups').filter(is_superuser=False)

        for user in queryset:
            if request.user.is_superuser:
                user.groups.clear()
            else:
                user.groups.remove(self.users_group, self.verified_users_group)

        for key in request.POST.keys():
            if not key.startswith('csrf'):
                checkbox_on = key.split('_')
                group = checkbox_on[0]
                username = checkbox_on[1]
                user = queryset.get(username=username)
                user.groups.add(Group.objects.get(name=group))
        return redirect(reverse('app_users:users_list'))

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = User.objects.prefetch_related('groups').filter(is_superuser=False)
        context = super().get_context_data(**kwargs)
        context['moderators_group'] = []
        context['verifiedusers_group'] = []
        context['users_group'] =[]
        for user in queryset:
            if user.groups.contains(self.users_group):
                context['users_group'].append(user.username)
            if user.groups.contains(self.moderator_group):
                context['moderators_group'].append(user.username)
            if user.groups.contains(self.verified_users_group):
                context['verifiedusers_group'].append(user.username)
        return context
