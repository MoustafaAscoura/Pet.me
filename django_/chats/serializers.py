from rest_framework import serializers
from .models import *

class MessageSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        data = super(MessageSerializer, self).to_representation(obj)

        return {
            "message_id": obj.id,
            "sender": obj.sender.full_name,
            "sender_id": obj.sender.id,
            "sender_picture": data['sender']['picture'],
            "receiver": obj.receiver.full_name,
            "receiver_id": obj.receiver.id,
            "receiver_picture": data['receiver']['picture'],
            "content": obj.content,
            "created_at": obj.created_at,
        }
    class Meta:
        model = Message
        fields = '__all__'
        depth = 1
        read_only_fields = ('created_at','sender','receiver')


        