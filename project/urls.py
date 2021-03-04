from django.urls import path
from .views import ProjectList, ProjectDetail

app_name = 'project'
urlpatterns = [
    path('list/', ProjectList.as_view(), name='list'),
    path('detail/<int:pk>', ProjectDetail.as_view(), name='detail'),
]