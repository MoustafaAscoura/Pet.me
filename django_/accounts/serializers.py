from rest_framework import serializers
import re
from django.core.files.images import get_image_dimensions

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
    
    def validate_picture(self, picture):
        w, h = get_image_dimensions(picture)

        if (picture and picture.size > 2000000) :
            raise serializers.ValidationError("Image size should be less than 2 Mbs")
        elif w < 400 or h < 400:
            raise serializers.ValidationError("Image dimensions should be greater than 400 pixels")

        return picture
    
        
    def validate_phone(self, phone):
        re.compile('^01[0125]{1}[0-9]{8}$')
        if re.fullmatch('^01[0125]{1}[0-9]{8}$',phone) or phone=="":
            return phone
        else:
            raise serializers.ValidationError("Phone must match Egyptian format")


