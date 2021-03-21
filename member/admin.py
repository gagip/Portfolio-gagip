from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Profile

class ProfileAdmin(admin.StackedInline):
    model = Profile
    on_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = [ProfileAdmin, ]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)