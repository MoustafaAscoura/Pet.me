from rest_framework import serializers
from .models import Offer,AdoptRequest
from pets.serializers import PetSerializer
from chats.serializers import MessageSerializer

class AdoptRequestsSerializer(serializers.ModelSerializer):
    message = MessageSerializer()
    def to_representation(self, obj):
        return {
            "request_id": obj.id,
            "username": obj.user.full_name,
            "user_id": obj.user.id, 
            "user_picture": obj.user.get_profile_picture(),
            "petname": obj.offer.pet.name,
            "pet_id": obj.offer.pet.id,
            "created_at": obj.created_at,
            "message":obj.message.content,
        }

    class Meta:
        model = AdoptRequest
        fields='__all__'
        read_only_fields = ('id','created_at',  )



class OfferSerializer(serializers.ModelSerializer):
    pet = PetSerializer(read_only=True)

    class Meta:
        model = Offer
        fields = '__all__'
