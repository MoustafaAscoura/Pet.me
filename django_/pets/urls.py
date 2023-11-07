from django.urls import path
from .views import *


urlpatterns = [
    path('', PetsView.as_view({'get': 'list', 'post':'create'}) ,name='pets'),
    path('<int:pk>', 
         PetsView.as_view({'get': 'retrieve',
                             'post':'update', 'delete':'destroy'}) ,name='pets.details'),          
    path('<int:pk>/adoptions', PetAdoptionsView.as_view({'get': 'list', 'post':'create'}), name='pets.history'),
    path('<int:pk>/offer', PetsView.as_view({'get':'offerPet'}), name="pets.offer")
]