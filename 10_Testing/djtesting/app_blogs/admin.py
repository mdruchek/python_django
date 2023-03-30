from django.contrib import admin
from app_blogs.models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass
