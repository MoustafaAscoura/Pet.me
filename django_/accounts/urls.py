from django.urls import path, include
from .views import *

urlpatterns = [
    path('<int:id>/adoptions', UserAdoptionsView.as_view({'get': 'list'}), name='user.history'),
]
