from django.shortcuts import render
from django.utils import timezone
from rest_framework import viewsets
from .models import Pet, Adoption
from .serializers import PetSerializer, AdoptionSerializer
# Create your views here.

class PetsView(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def perform_create(self, serializer):
        pet = serializer.save(owner=self.request.user)
        adoption = Adoption(user=self.request.user, pet=pet)
        adoption.save()

class PetAdoptionsView(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Adoption.objects.filter(pet__id=self.kwargs['id'])
    serializer_class = AdoptionSerializer

    def perform_create(self, serializer):
        latest_adoption = self.queryset.last()
        latest_adoption.end_at = timezone.now()

        serializer.save(owner=self.request.user)

