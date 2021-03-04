from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    meta_description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("project:project_in_category", kwargs={"slug": self.slug})
    

# Create your models here.
class Project(models.Model):
    cate = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='projects')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    tech = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to='project/')
    
    class Meta:
        ordering = ['-start_date', '-title',]
        index_together = [['id', 'slug']]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project:detail", kwargs={"pk": self.pk})
    

    

