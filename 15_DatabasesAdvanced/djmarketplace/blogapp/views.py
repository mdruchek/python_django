from django.shortcuts import render
from django.views.generic import ListView
from .models import Article
import logging


logger = logging.getLogger(__name__)


def articles_list_view(request):
    articles = (Article.objects
                .select_related('author', 'category')
                .prefetch_related('tags')
                .defer('content', 'author__id', 'author__bio')
                .order_by('-pub_date')
                .all())
    logger.info('Собрали blogs в articles')

    context = {'articles': articles}
    logger.info('Передали articles в context')

    return render(request, 'blogapp/article_list.html', context=context)
