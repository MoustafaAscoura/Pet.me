from django.urls import path, include
from .views import *

# urlpatterns = [
#     path('<int:id>/adoptions', UserAdoptionsView.as_view({'get': 'list'}), name='user.history'),
# ]


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/<int:id>/adoptions', UserAdoptionsView.as_view({'get': 'list'}), name='user.history'),
]