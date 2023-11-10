from django.urls import path
from .views import *

urlpatterns = [
    path('', OffersView.as_view({'get': 'list'}) ,name='offers'),

    path('<int:pk>',
         OffersView.as_view({'get': 'retrieve','delete':'destroy'}) ,name='offers.details'),

    #all requests for all offers (of the current user)
    path('requests', AdoptRequestsView.as_view({'get': 'list'}),name='requests'),

    #requests for this only offer
    path('<int:offer_id>/requests', AdoptRequestsView.as_view({ 'get':'list','post': 'requestAdopt'}),name='requests.create'),
    
    path('request/<int:pk>',
         AdoptRequestsView.as_view({'get': 'retrieve','delete':'destroy'}), name='requests.details'),
    path('request/<int:pk>/accept', 
         AdoptRequestsView.as_view({'get':'accept'}),name='requests.accept'),
    path('request/<int:pk>/reject',
         AdoptRequestsView.as_view({'get':'destroy'}),name='requests.reject')
]