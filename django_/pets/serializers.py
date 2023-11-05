from rest_framework import serializers
from .models import Pet, Adoption


class PetSerializer(serializers.Serializer):
    class Meta:
        model = Pet
        fields = '__all__'


class AdoptionSerializer(serializers.Serializer):
    class Meta:
        model = Adoption
        fields = '__all__'