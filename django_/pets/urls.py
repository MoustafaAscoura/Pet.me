from django.urls import path
from .views import *


urlpatterns = [
    path('', PetList.as_view(), name='pet-list' ),
    path('', PetList.as_view(), name='pet-list' ),
    path('', PetList.as_view(), name='pet-list' ),
    path('', PetList.as_view(), name='pet-list' ),
]