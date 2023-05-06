from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from app_housing.models import News, Housing


class NewsSitemap(Sitemap):
    changefreg = 'weekly'
    priority = 0.9

    def items(self):
        return News.objects.all()

    def lastmod(self, obj):
        return obj.published_at


class HousingSitemap(Sitemap):
    changefreg = 'weekly'
    priority = 0.9

    def items(self):
        return Housing.objects.all()

    def lastmod(self, obj):
        return obj.created_at


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['about', 'contacts']

    def location(self, item):
        return reverse(item)
