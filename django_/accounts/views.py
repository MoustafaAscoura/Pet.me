from django.shortcuts import render
from rest_framework import viewsets

from pets.models import Adoption
from pets.serializers import AdoptionSerializer

# Create your views here.
class UserAdoptionsView(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Adoption.objects.filter(user__id=self.kwargs['id'])
    serializer_class = AdoptionSerializer