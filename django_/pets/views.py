from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Pet, Adoption, Photo
from offers.models import Offer
from .serializers import PetSerializer, AdoptionSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

# Create your views here.

class PetsView(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def perform_create(self, serializer):
        pet = serializer.save(owner=self.request.user)
        adoption = Adoption(user=self.request.user, pet=pet)
        adoption.save()

        files = self.request.FILES.getlist('photos')
        if files:
            [Photo.objects.create(pet=pet,photo=f) for f in files]
        else:
            if serializer.data.get('pet_type') == 'Cat':
                Photo.objects.create(pet=pet,photo="/media/pets/images/cat_annon.png")
            else:
                Photo.objects.create(pet=pet,photo="/media/pets/images/dog_annon.png")

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
        return Response('Pet is offered for adoption', status=status.HTTP_201_CREATED)


class PetAdoptionsView(viewsets.ModelViewSet):
    def get_queryset(self):
        return Adoption.objects.filter(pet__id=self.kwargs['pk'])
    serializer_class = AdoptionSerializer


