from .views import LoginView, RegisterView, ProfileView, LogoutView

from django.urls import path


urlpatterns = [
    # Urls de l'authentification
    path('account/register/', RegisterView.as_view(), name='register'),
    path('account/login/', LoginView.as_view(), name='login'),
    path('account/logout/', LogoutView.as_view(), name='logout'),
    # Urls du profile
    path('account/profiles/', ProfileView.as_view(), name='profile-list'),
    path('account/profiles/<int:pk>/', ProfileView.as_view(), name='profile')
]