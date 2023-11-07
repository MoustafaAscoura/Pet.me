from rest_framework import serializers
from .models import *
from accounts.serializers import UserSerializer

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('photo',)

class AdoptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adoption
        fields = '__all__'
    
    def to_representation(self, obj):
        return {
            "username": obj.user.full_name,
            "user_id": obj.user.id, 
            "petname": obj.pet.name,
            "pet_id": obj.pet.id,
            "start_at": obj.start_at,
            "end_at": obj.end_at
        }

class PetSerializer(serializers.ModelSerializer):
    thumbnail = serializers.CharField(source='get_thumbnail', read_only=True)
    age = serializers.CharField(source='get_age', read_only=True)
    owner = UserSerializer(read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)
    adoptions = AdoptionSerializer(many=True, read_only=True)

    class Meta:
        model = Pet
        fields = '__all__'
        read_only_fields = ('id', 'created_at')
        extra_kwargs = {
            'password': {'write_only': True},
            'birthdate': {'write_only': True},
        }
        