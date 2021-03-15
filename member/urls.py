from django.urls import path
from django.contrib.auth import views as auth_view
from .views import login, logout, signup

app_name = 'member'
urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('signup/', signup, name='signup'),
    # path('signup/')
]