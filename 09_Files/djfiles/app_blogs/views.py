from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog
from .forms import BlogForm


class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    ordering = ['-created']


class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog'

class CreateBlogView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = 'content', 'image
