from django.contrib import admin
from advertisements_app.models import Advertisements, AdvertisementAuthor, AdvertisementCategory, AdvertisementType

# Register your models here.


@admin.register(Advertisements)
class AdvertisementsAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvertisementAuthor)
class AdvertisementAuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvertisementCategory)
class AdvertisementCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvertisementType)
class AdvertisementTypeAdmin(admin.ModelAdmin):
    pass
