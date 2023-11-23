from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db import IntegrityError

from django.utils import timezone
from rest_framework import viewsets
from .models import Offer,AdoptRequest
from pets.models import Adoption
from chats.models import Message
from social.models import Post, Photo
from .serializers import OfferSerializer,AdoptRequestsSerializer
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from .permissons import OfferPermission, RequestPermission

class OffersView(viewsets.ModelViewSet):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    search_fields=['pet__name', 'user__username', 'description','pet__species','pet__breed']
    permission_classes = [OfferPermission]

    def get_queryset(self):
        alloffers = Offer.objects.all()
        species = self.request.query_params.get('species')
        gender = self.request.query_params.get('gender')

        if gender: alloffers = alloffers.filter(pet__gender=gender)
        if species: alloffers = alloffers.filter(pet__species=species.capitalize())

        return alloffers
    
    serializer_class = OfferSerializer        

class AdoptRequestsView(viewsets.ModelViewSet):
    permission_classes = [RequestPermission]
    def get_queryset(self):
        if self.kwargs.get('offer_id'):
            return AdoptRequest.objects.filter(offer__id=self.kwargs['offer_id'])

        return AdoptRequest.objects.filter(offer__user=self.request.user)

    serializer_class = AdoptRequestsSerializer

    def requestAdopt(self, request, offer_id):
        message = request.data.get('message', 'I request to adopt this pet!')
        user=request.user
        offer=get_object_or_404(Offer,pk=self.kwargs['offer_id'])
        message_ = Message.objects.create(sender=user, receiver=offer.user,content=message)

        try:
            req = AdoptRequest.objects.create(user=user, offer=offer,message=message_)
        except IntegrityError:
            message_.delete()
            return Response("You already have a request", status=status.HTTP_400_BAD_REQUEST)

        return Response("Request sent successfully",status=status.HTTP_201_CREATED)

    def accept(self,request, pk):
        adopt_request = self.get_object()
        adopt_offer = adopt_request.offer
        pet = adopt_offer.pet
        old_owner = pet.owner
        
        #end ownership of old owner and create new adoption for new owner
        adoption = pet.adoptions.last()
        adoption.end_at = timezone.now().date()
        adoption.save()

        pet.owner = adopt_request.user
        pet.save()
        
        new_adoption = Adoption(user=adopt_request.user, pet=pet)
        new_adoption.save()
        adopt_offer.delete()

        post = Post.objects.create(user=pet.owner, content=f"Say hello to my new pet, {pet.name}! I just adopted him from {old_owner}!", )
        photo = Photo.objects.create(photo=pet.photos.first().photo, post=post)

        return Response('Accepted Adopt Request', status=status.HTTP_204_NO_CONTENT)
        
