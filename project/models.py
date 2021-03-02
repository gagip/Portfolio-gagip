from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Project(models.Model):
    title = models.CharField(max_length=200)
    cate = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    tech = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to='project/')
    
    class Meta:
        ordering = ['start_date', 'title',]
        
    def __str__(self):
        return self.title
    

