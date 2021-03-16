from django.urls import path
from .views import *

app_name = 'board'
urlpatterns = [
    path('', BoardListView.as_view(), name='board_list'),
    path('detail/<int:pk>/', BoardDetailView.as_view(), name='board_detail'),
    path('upload/', BoardCreateView.as_view(), name='board_upload'),
    path('delete/<int:pk>/', BoardDeleteView.as_view(), name='board_delete'),
    path('update/<int:pk>/', BoardUpdateView.as_view(), name='board_update'),
    path('comment/<int:board_id>/', comment_create, name='comment_create'),
]