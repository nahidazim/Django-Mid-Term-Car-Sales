from django.urls import path
from .views import register, login_view, profile, logout_view, edit_profile, change_password

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/change_password/', change_password, name='change_password'),
    path('logout/', logout_view, name='logout'),
]
