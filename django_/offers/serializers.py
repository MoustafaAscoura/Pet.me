from rest_framework import serializers
from .models import Offer,AdoptRequest
from pets.serializers import PetSerializer

class AdoptRequestsSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        return {
            "request_id": obj.id,
            "username": obj.user.full_name,
            "user_id": obj.user.id, 
            "user_picture": obj.user.get_profile_picture(),
            "petname": obj.offer.pet.name,
            "pet_id": obj.offer.pet.id,
            "created_at": obj.created_at,
        }

    class Meta:
        model = AdoptRequest

class OfferSerializer(serializers.ModelSerializer):
    pet = PetSerializer(read_only=True)
    requests = AdoptRequestsSerializer(many=True, read_only=True)
    class Meta:
        model = Offer
        fields = '__all__'
        read_only_fields = ('available','created_at')