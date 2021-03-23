from django.urls import path, include
from .views import index

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
]