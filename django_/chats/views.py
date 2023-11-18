from django.db.models import Q
from rest_framework import viewsets, pagination
from django.http import JsonResponse
from itertools import chain

from accounts.models import User
from .serializers import *
from .models import *

from rest_framework.permissions import IsAuthenticated
from .permissons import UserPermission

class MessagesView(viewsets.ModelViewSet):
    search_fields=['content']
    pagination.PageNumberPagination.page_size = 50 
    permission_classes = [IsAuthenticated, UserPermission]

    def get_queryset(self):
        curr_user = self.request.user

        if self.kwargs.get('user_id'):
            other_user = self.kwargs['user_id']
            criteria1 = Q(sender=curr_user) & Q(receiver=other_user)
            criteria2 = Q(sender=other_user) & Q(receiver=curr_user)

            return Message.objects.filter(Q(criteria1) | Q(criteria2))

    def relatedUsers(self, request):
        curr_user = self.request.user
        people1 = curr_user.sent_messages.values_list('receiver__id','receiver__picture',
                                         'receiver__username', 'receiver__first_name', 'receiver__last_name')
        people2 = curr_user.received_messages.values_list('sender__id','sender__picture','sender__username', 'sender__first_name',
                                         'sender__last_name')
        

        result_list = set(chain(people1, people2))
        keys=["id","picture","username","first_name","last_name"]
        return JsonResponse([dict(zip(keys,person)) for person in result_list], safe=False)

    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        receiver = User.objects.filter(id=self.kwargs['user_id']).first()
        serializer.save(sender=self.request.user, receiver=receiver)
