from django.shortcuts import render
from django.http import HttpResponse


def advertisement_list(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_list.html', {})


def python(request, *args, **kwargs):
    return render(request, 'advertisement/python.html', {})


def java(request, *args, **kwargs):
    return render(request, 'advertisement/java.html', {})


def web_layout(request, *args, **kwargs):
    return render(request, 'advertisement/web_layout.html', {})


def devops(request, *args, **kwargs):
    return render(request, 'advertisement/devops.html', {})


def cpp(request, *args, **kwargs):
    return render(request, 'advertisement/cpp.html')
