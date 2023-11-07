from django.shortcuts import render
from django.utils import timezone
from rest_framework import viewsets
from .models import Pet, Adoption, Photo
from .serializers import PetSerializer, AdoptionSerializer
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
        pet = serializer.save(owner=self.request.user)
        files = self.request.FILES.getlist('photos')
        if files:
            for old_photo in pet.photos: old_photo.delete()
            for f in files: Photo.objects.create(pet=pet,photo=f)

class PetAdoptionsView(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Adoption.objects.filter(pet__id=self.kwargs['id'])
    serializer_class = AdoptionSerializer

    def perform_create(self, serializer):
        latest_adoption = self.queryset.last()
        latest_adoption.end_at = timezone.now().date()
        serializer.save(owner=self.request.user)

