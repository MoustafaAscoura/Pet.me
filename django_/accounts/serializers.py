# users/serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','first_name', 'last_name', 'email', 'gender', 'password','phone','picture','birthdate','profile_url','created_at']
        read_only_fields = ('id', 'created_at',)
        extra_kwargs = {
            'password': {'write_only': True}
        }

