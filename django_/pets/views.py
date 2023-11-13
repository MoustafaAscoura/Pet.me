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
    search_fields=['name', 'pet_type', 'species']
    ordering_fields=['birthdate']

    def get_queryset(self):
        allpets = Pet.objects.all()
        pet_type = self.request.query_params.get('pet_type')
        gender = self.request.query_params.get('gender')
        if gender: allpets = allpets.filter(gender__icontains=gender)
        if pet_type: allpets = allpets.filter(pet_type__icontains=pet_type)

        return allpets

        
    serializer_class = PetSerializer
    permission_classes = [UserPermission]

    def create(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data['owner'] = request.user.id
        request.data._mutable = False
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data['owner'] = request.user.id
        request.data._mutable = False
        return super().update(request, *args, **kwargs)

    def perform_create(self, serializer):
        pet = serializer.save()
        adoption = Adoption(user=self.request.user, pet=pet)
        adoption.save()

        files = self.request.FILES.getlist('photos')
        if files:
            [Photo.objects.create(pet=pet,photo=f) for f in files]
        else:
            if serializer.data.get('pet_type') == 'Cat':
                Photo.objects.create(pet=pet,photo="pets/images/cat_annon.png")
            else:
                Photo.objects.create(pet=pet,photo="pets/images/dog_annon.png")

    def perform_update(self,serializer):
        pet = serializer.save()
        files = self.request.FILES.getlist('photos')
        if files:
            for old_photo in pet.photos.all(): old_photo.delete()
            for f in files: Photo.objects.create(pet=pet,photo=f)

    def offerPet(self, request, pk):
        offer = Offer.objects.create(
            user=request.user, pet=get_object_or_404(Pet,pk=self.kwargs['pk']), 
                                                    description=request.data.get('description'))
        post = Post.objects.create(user=request.user, content=f"Hi, I am offering my pet, {offer.pet.name}, for adoption!")
        return Response('Pet is offered for adoption', status=status.HTTP_201_CREATED)


