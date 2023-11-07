from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from django.utils import timezone
from rest_framework import viewsets
from .models import Offer,AdoptRequest
from pets.models import Adoption
from .serializers import OfferSerializer,AdoptRequestsSerializer


class OffersView(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer        

class AdoptRequestsView(viewsets.ModelViewSet):
    def get_queryset(self):
        return AdoptRequest.objects.filter(offer__user=self.request.user)

    serializer_class = AdoptRequestsSerializer

    def requestAdopt(self, request, pk):
        req = AdoptRequest.objects.create(user=request.user, offer=get_object_or_404(Offer,pk=self.kwargs['pk']))
        return Response('Your request was sent', status=status.HTTP_201_CREATED)

    def accept(self,request, pk):
        adopt_request = self.get_object()
        adopt_offer = adopt_request.offer
        pet = adopt_offer.pet
        owner = pet.owner

        #end ownership of old owner and create new adoption for new owner
        adoption = pet.adoptions.last()
        adoption.end_date = timezone.now().date()
        adoption.save()

        pet.owner = adopt_request.user
        pet.save()
        
        adopt_offer.available = False
        adopt_offer.save()
        adopt_request.delete()
        new_adoption = Adoption(user=adopt_request.user, pet=pet)
        new_adoption.save()
        return Response('Accepted Adopt Request', status=status.HTTP_204_NO_CONTENT)
