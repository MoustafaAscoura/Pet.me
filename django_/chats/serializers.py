from rest_framework import serializers
from .models import *

class MessageSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        return {
            "message_id": obj.id,
            "sender": obj.sender.full_name,
            "sender_id": obj.sender.id,
            "sender_picture": obj.sender.get_profile_picture(),
            "receiver": obj.receiver.full_name,
            "receiver_id": obj.receiver.id,
            "receiver_picture": obj.receiver.get_profile_picture(),
            "content": obj.content,
            "created_at": obj.created_at,
        }
    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ('created_at','sender','receiver')


        