from django.urls import path
from .views import *

urlpatterns = [
    path('', OffersView.as_view({'get': 'list'}) ,name='offers'),

    path('<int:pk>',
         OffersView.as_view({'get': 'retrieve','delete':'destroy'}) ,name='offers.details'),

    path('requests', AdoptRequestsView.as_view({'get': 'list'}),name='requests'),
    path('<int:pk>/request', AdoptRequestsView.as_view({'get': 'requestAdopt'}),name='requests.create'),
    
    path('requests/<int:pk>',
         AdoptRequestsView.as_view({'get': 'retrieve','delete':'destroy'}), name='requests.details'),
    path('requests/<int:pk>/accept', 
         AdoptRequestsView.as_view({'get':'accept'}),name='requests.accept'),
    path('requests/<int:pk>/reject',
         AdoptRequestsView.as_view({'get':'destroy'}),name='requests.reject')
]