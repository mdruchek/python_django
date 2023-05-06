from django.contrib.syndication.views import Feed
from django.urls import reverse
from app_housing.models import News


class LatestNewsFeed(Feed):
    title = 'Новости'
    link = '/sitenews/'
    description = 'Самые свежие новости.'

    def items(self):
        return News.objects.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return reverse('news_detail', args=[item.pk])
