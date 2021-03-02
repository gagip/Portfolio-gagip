from django.urls import path, include
from .views import index, introduce

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('introduce/', introduce, name='introduce'),
]