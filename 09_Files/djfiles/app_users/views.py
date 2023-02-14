from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class AuthUsersView(LoginView):
    template_name = 'app_users/login.html'
    next_page = ''


def registration_view(request):
    form = UserCreationForm()
    context = {
            'form': form
    }
    return render(request, 'app_users/registration.html', context=context)
