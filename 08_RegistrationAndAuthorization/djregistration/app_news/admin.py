from django.contrib import admin
from .models import NewsModel, CommentModel


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = 'title', 'author', 'archived', 'date_creation', 'date_edit'
    list_display_links = 'title',
    fields = 'title', 'content_news', 'archived'
    ordering = '-date_creation',

    def get_queryset(self, request):
        return NewsModel.objects.select_related("author")
