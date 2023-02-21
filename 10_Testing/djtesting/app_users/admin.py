from django.contrib import admin
from .models import ProfileUser

class ProfileUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'avatar',)


admin.site.register(ProfileUser, ProfileUserAdmin)
