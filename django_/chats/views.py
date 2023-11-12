from django.db.models import Q
from rest_framework import viewsets, pagination

from accounts.models import User
from .serializers import *
from .models import *

class MessagesView(viewsets.ModelViewSet):
    search_fields=['content']
    pagination.PageNumberPagination.page_size = 50 

    def get_queryset(self):
        curr_user = self.request.user
        other_user = self.kwargs['user_id']
        criteria1 = Q(sender=curr_user) & Q(receiver=other_user)
        criteria2 = Q(sender=other_user) & Q(receiver=curr_user)

        return Message.objects.filter(Q(criteria1) | Q(criteria2))
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        receiver = User.objects.filter(id=self.kwargs['receiver_id']).first()
        serializer.save(sender=self.request.user, receiver=receiver)
