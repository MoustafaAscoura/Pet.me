# # users/serializers.py
# from rest_framework import serializers
# from .models import User
# # from pets.serializers import AdoptionSerializer, PetSerializer

# class UserSerializer(serializers.ModelSerializer):
#     # adoptions = AdoptionSerializer(many=True, read_only=True)
#     # pets = PetSerializer(many=True, read_only=True)
    
#     class Meta:
#         model = User
#         fields = ['id', 'username','first_name', 'last_name', 'email', 'gender', 'password','phone','picture','birthdate','profile_url','created_at']
#         read_only_fields = ('id', 'created_at',)
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }

# -----------------------------------------------------------
# # users/serializers.py
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("id", "email", "username", "first_name", "last_name", "password")
