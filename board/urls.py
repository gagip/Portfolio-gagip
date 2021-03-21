from django.urls import path
from .views import *

app_name = 'board'
urlpatterns = [
    # 게시판 관련 URL
    path('', BoardListView.as_view(), name='board_list'),
    path('detail/<int:pk>/', BoardDetailView.as_view(), name='board_detail'),
    path('upload/', BoardCreateView.as_view(), name='board_upload'),
    path('delete/<int:pk>/', BoardDeleteView.as_view(), name='board_delete'),
    path('update/<int:pk>/', BoardUpdateView.as_view(), name='board_update'),
    path('search/', search, name='search'),
    # 댓글 관련 URL
    path('comment/create/<int:board_id>/', comment_create, name='comment_create'),
    path('comment/delete/<int:comment_id>/', comment_delete, name='comment_delete'),
    path('comment/update/<int:comment_id>/', comment_update, name='comment_update'),
]