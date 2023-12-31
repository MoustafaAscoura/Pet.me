from django.urls import path
from .views import PetsView


urlpatterns = [
    path('', PetsView.as_view({'get': 'list', 'post':'create'}) ,name='pets'),
    path('<int:pk>/', 
         PetsView.as_view({'get': 'retrieve', 'patch':'partial_update',
                             'post':'update', 'delete':'destroy'}) ,name='pets.details'),
                                    
    path('<int:pk>/offer/', PetsView.as_view({'post':'offerPet'}), name="pets.offer")
]