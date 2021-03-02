from django.contrib import admin
from .models import Photo, Post

# Register your models here.
class PhotoInline(admin.TabularInline):
    model = Photo

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]
