from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import LoginView, ProfileView, RegisterView, UpdateProfileView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/<int:user_id>/', ProfileView.as_view(), name='profile'),
    path('update_profile/', UpdateProfileView.as_view(), name='update_profile')
]
