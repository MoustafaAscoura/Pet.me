from rest_framework import serializers

from .models import User
from pets.serializers import PetSerializer, AdoptionSerializer
from social.serializers import PostsSerializer

class UserSerializer(serializers.ModelSerializer):
    pets = PetSerializer(many=True, read_only=True)
    adoptions = AdoptionSerializer(many=True, read_only=True)
    posts = PostsSerializer(many=True, read_only=True)

    def to_representation(self, obj):
        data = super(UserSerializer, self).to_representation(obj)
        for pet in data['pets']:
            del pet['owner'], pet['adoptions'], pet['photos']
        for post in data['posts']:
            del post['comments'], post['user']

        return data
    
    class Meta:
        model = User
        # fields = '__all__' #['id', 'username','first_name', 'last_name', 'email', 'gender', 'password','phone','picture','birthdate','profile_url','created_at', 'pets']
        exclude = ('last_login', 'is_staff', 'is_active', 'groups', 'user_permissions')
        read_only_fields = ('id', 'created_at','email','username')
        depth = 1
        extra_kwargs = {
            'password': {'write_only': True}
        }
