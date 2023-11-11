from django.urls import path, include
from .views import *

urlpatterns = [
    path('users/activate/<uid>/<token>', ActivateUser.as_view({'get': 'activation'}), name='emailactivate'),
    path('<int:id>/adoptions', UserAdoptionsView.as_view({'get': 'list'}), name='user.history'),

    #temporary view - to be deleted later
    path('social/complete/<provider>/', SocialAuthCompleteView.as_view(), name="social-auth-complete"),

    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('', include('djoser.social.urls')),
]