from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from django.utils import timezone
from rest_framework import viewsets
from .models import Offer,AdoptRequest
from pets.models import Adoption
from chats.models import Message
from .serializers import OfferSerializer,AdoptRequestsSerializer


class OffersView(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer        

class AdoptRequestsView(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.kwargs.get('offer_id'):
            return AdoptRequest.objects.filter(offer__id=self.kwargs['offer_id'])

        return AdoptRequest.objects.filter(offer__user=self.request.user)

    serializer_class = AdoptRequestsSerializer

    def requestAdopt(self, request, pk):
        message = request.data.get('message', 'I request to adopt this pet!')
        user=request.user
        offer=get_object_or_404(Offer,pk=self.kwargs['pk'])

        if not offer.available:
            return Response("Offer is no more available",status=status.HTTP_400_BAD_REQUEST)
        elif user == offer.user:
            return Response("Cannot Perform request on owned offer",status=status.HTTP_400_BAD_REQUEST)

        message_ = Message.objects.create(sender=user, receiver=offer.user,content=message)
        req = AdoptRequest.objects.create(user=user, offer=offer,message=message_)
        
        return Response("Request sent successfully",status=status.HTTP_201_CREATED)

    def accept(self,request, pk):
        adopt_request = self.get_object()
        adopt_offer = adopt_request.offer
        pet = adopt_offer.pet
        owner = pet.owner

        #end ownership of old owner and create new adoption for new owner
        adoption = pet.adoptions.last()
        adoption.end_at = timezone.now().date()
        adoption.save()

        pet.owner = adopt_request.user
        pet.save()
        
        adopt_offer.available = False
        adopt_offer.save()
        adopt_request.delete()
        new_adoption = Adoption(user=adopt_request.user, pet=pet)
        new_adoption.save()
        return Response('Accepted Adopt Request', status=status.HTTP_204_NO_CONTENT)
