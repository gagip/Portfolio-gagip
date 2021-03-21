from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import login, logout, signup, profile, member_delete, profile_update

app_name = 'member'
urlpatterns = [
    # 계정 관련 URL
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('signup/', signup, name='signup'),
    path('delete/', member_delete, name='member_delete'),

    # 프로필 관련 URL
    path('profile/<int:user_id>', profile, name='profile'),
    path('profile/update/', profile_update, name='profile_update'),
    # path('signup/')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)