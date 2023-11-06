from rest_framework import serializers
from .models import Pet, Adoption
from accounts.serializers import UserSerializer

class PetSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Pet
        fields = '__all__'
        


class AdoptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adoption
        fields = '__all__'