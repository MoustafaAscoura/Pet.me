from django.shortcuts import render
from rest_framework import generics
from .models import Pet, Adoption
from .serializers import PetSerializer, AdoptionSerializer
# Create your views here.

class PetList(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class PetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class AdoptionList(generics.ListCreateAPIView):
    queryset = Adoption.objects.all()
    serializer_class = AdoptionSerializer

class AdoptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Adoption.objects.all()
    serializer_class = AdoptionSerializer
