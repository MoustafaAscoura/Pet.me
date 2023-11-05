from django.urls import path
from djoser import views as djoser_views

urlpatterns = [
    path('auth/login/', djoser_views.LoginView.as_view(), name='login'),
    path('auth/register/', djoser_views.RegistrationView.as_view(), name='register'),
]
