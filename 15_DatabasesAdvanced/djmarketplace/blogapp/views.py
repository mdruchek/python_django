from django.shortcuts import render
from django.views.generic import ListView
from .models import Article


class ArticleListView(ListView):
    queryset = (Article.objects
                .select_related('author', 'category')
                .prefetch_related('tags').all()
                .defer('content')
                .order_by('-pub_date'))
    context_object_name = 'articles'
