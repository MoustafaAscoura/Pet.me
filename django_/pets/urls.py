from django.urls import path
from .views import *


urlpatterns = [
    path('', PetsView.as_view({'get': 'list', 'post':'create'}) ,name='pets'),
    path('<int:pk>', 
         PetsView.as_view({'get': 'retrieve',
                             'post':'update', 'delete':'destroy'}) ,name='pets.details'),
                             
    path('<int:id>/adoptions', PetAdoptionsView.as_view({'get': 'list', 'post':'create'}), name='pets.history'),
]