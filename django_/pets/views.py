from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Pet, Adoption, Photo
from offers.models import Offer
from social.models import Post
from .serializers import PetSerializer, AdoptionSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from .permissons import UserPermission


# Create your views here.

class PetsView(viewsets.ModelViewSet):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    search_fields=['name', 'species']
    ordering_fields=['birthdate', 'created_at']
    ordering = ['-created_at']


    def get_queryset(self):
        allpets = Pet.objects.all()
        species = self.request.query_params.get('species')
        gender = self.request.query_params.get('gender')
        if gender: allpets = allpets.filter(gender=gender)
        if species: allpets = allpets.filter(species=species.capitalize())
        return allpets

        
    serializer_class = PetSerializer
    permission_classes = [UserPermission]

    def perform_create(self, serializer):
        pet = serializer.save()
        adoption = Adoption(user=self.request.user, pet=pet)
        adoption.save()

        files = self.request.FILES.getlist('photos')
        if files:
            [Photo.objects.create(pet=pet,photo=f) for f in files[0:4]]
        else:
            if serializer.data.get('species') == 'Cat':
                Photo.objects.create(pet=pet,photo="pets/images/cat_annon.png")
            else:
                Photo.objects.create(pet=pet,photo="pets/images/dog_annon.png")

    def perform_update(self,serializer):
        pet = serializer.save()
        files = self.request.FILES.getlist('photos')
        if files:
            for old_photo in pet.photos.all(): old_photo.delete()
            for f in files[0:4]: Photo.objects.create(pet=pet,photo=f)

    def offerPet(self, request, pk):
        offer = Offer.objects.create(
            user=request.user, pet=get_object_or_404(Pet,pk=self.kwargs['pk']), 
                                                    description=request.data.get('description'))
        post = Post.objects.create(user=request.user, visible=True, content=f"Hi, I am offering my pet, {offer.pet.name}, for adoption!")
        return Response('Pet is offered for adoption', status=status.HTTP_201_CREATED)


