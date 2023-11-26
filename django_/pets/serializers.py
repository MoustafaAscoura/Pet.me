from rest_framework import serializers


from .models import *

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('photo',)

class AdoptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adoption
        fields = '__all__'
        depth = 1

    def to_representation(self, obj):
        data = super(AdoptionSerializer, self).to_representation(obj)
        return {
            "username": obj.user.full_name,
            "user_id": obj.user.id,
            "user_picture": data['user']['picture'],
            "petname": obj.pet.name,
            "pet_id": obj.pet.id,
            "start_at": obj.start_at,
            "end_at": obj.end_at
        }

class PetSerializer(serializers.ModelSerializer):
    thumbnail = serializers.CharField(source='get_thumbnail', read_only=True)
    age = serializers.CharField(source='get_age', read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)
    adoptions = AdoptionSerializer(many=True, read_only=True)

    def to_representation(self, obj):
        data = super(PetSerializer, self).to_representation(obj)
        data['owner'] = {
            "username": obj.owner.full_name,
            "user_id": obj.owner.id,
            "user_picture": data['owner']['picture'],   
        }
        
        data['offer'] = obj.offers.first().id if obj.offers.first() else 0

        if data['photos']:
            data['thumbnail'] = data['photos'][0]['photo']

        return data
    
    class Meta:
        model = Pet
        fields = '__all__'
        read_only_fields = ('id', 'created_at')
        depth = 1
        extra_kwargs = {
            'password': {'write_only': True},
        }
    
    def validate(self, attrs):
        attrs['owner'] = self.context['request'].user
        if attrs.get('birthdate') and attrs.get('birthdate') > timezone.now().date():
            raise serializers.ValidationError('Birthdate cannot be greater than today!')
        
        return attrs
