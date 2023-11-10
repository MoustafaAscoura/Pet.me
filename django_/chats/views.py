from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import *
from accounts.models import User
from .serializers import *

class MessagesView(viewsets.ModelViewSet):
    def get_queryset(self):
        return Message.objects.filter(Q(sender=self.request.user) | Q(receiver=self.request.user))
    serializer_class = MessageSerializer

    # def create(self, request, *args, **kwargs):
    #     request.data['receiver'] = User.objects.filter(id=self.kwargs['receiver_id']).first()
    #     request.data['sender'] = self.request.user
        
    #     serializer = self.get_serializer(data=request.data)
    #     print(serializer.__dict__)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        receiver = User.objects.filter(id=self.kwargs['receiver_id']).first()
        message = serializer.save(sender=self.request.user, receiver=receiver)
