from django.urls import path
from .views import *

urlpatterns = [
    path('', OffersView.as_view({'get': 'list', 'post':'create'}) ,name='offers'),
    path('<int:pk>', 
         OffersView.as_view({'get': 'retrieve',
                             'post':'update', 'delete':'destroy'}) ,name='offers.details'),

    path('<int:id>/requests', 
         AdoptRequestsView.as_view({'get': 'list', 'post':'create'}),name='requests'),
    path('<int:id>/requests/<int:pk>',
         AdoptRequestsView.as_view({'get': 'retrieve','delete':'destroy'}), name='requests.details'),
    path('<int:id>/requests/<int:pk>/accept', 
         AdoptRequestsView.as_view({'get':'accept'}),name='requests.accept'),
    path('<int:id>/requests/<int:pk>/reject',
         AdoptRequestsView.as_view({'get':'destroy'}),name='requests.reject')
]