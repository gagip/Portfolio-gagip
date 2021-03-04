from django.contrib import admin
from .models import Project, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug':['name']}

admin.site.register(Category, CategoryAdmin)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'cate', 'slug', 'description', 'tech']
    prepopulated_fields = {'slug':['title']}