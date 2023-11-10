from django.db.models import Q
from rest_framework import viewsets

from accounts.models import User
from .serializers import *
from .models import *

class MessagesView(viewsets.ModelViewSet):
    def get_queryset(self):
        return Message.objects.filter(Q(sender=self.request.user) | Q(receiver=self.request.user))
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        receiver = User.objects.filter(id=self.kwargs['receiver_id']).first()
        serializer.save(sender=self.request.user, receiver=receiver)
