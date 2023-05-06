from django.contrib import admin
from .models import News, TypeHousing, Room, Housing


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = 'title', 'published_at'


@admin.register(TypeHousing)
class TypeHousingAdmin(admin.ModelAdmin):
    pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(Housing)
class HousingAdmin(admin.ModelAdmin):
    pass
