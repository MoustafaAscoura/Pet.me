from django.urls import path, include
from .views import *

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.social.urls')),
    path('auth/users/activate/<uid>/<token>', ActivateUser.as_view({'get': 'activation'}), name='emailactivate'),
    path('<int:id>/adoptions', UserAdoptionsView.as_view({'get': 'list'}), name='user.history'),

    path('auth/social/login/<provider>/', SocialAuthView.as_view(), name="social-auth"),
    path('auth/social/complete/<provider>/', SocialAuthCompleteView.as_view(), name="social-auth-complete")
]