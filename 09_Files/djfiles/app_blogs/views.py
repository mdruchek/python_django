from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog


class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog'

class CreateBlog():

