from itertools import chain
from django.db.models import Q
from django.http import JsonResponse
from rest_framework import viewsets, pagination
from rest_framework.permissions import IsAuthenticated

from accounts.models import User
from .serializers import *
from .models import *
from .permissons import UserPermission

class MessagesView(viewsets.ModelViewSet):
    search_fields=['content']
    pagination.PageNumberPagination.page_size = 50 
    permission_classes = [IsAuthenticated, UserPermission]
    serializer_class = MessageSerializer

    def get_queryset(self):
        curr_user = self.request.user

        if self.kwargs.get('user_id'):
            other_user = self.kwargs['user_id']
            criteria1 = Q(sender=curr_user) & Q(receiver=other_user)
            criteria2 = Q(sender=other_user) & Q(receiver=curr_user)
            latest = Message.objects.filter(criteria2)
            if latest.exists():
                latest = latest.last()
                latest.seen = True
                latest.save()
            return Message.objects.filter(Q(criteria1) | Q(criteria2))
        return Message.objects.all()

    def relatedUsers(self, request):
        curr_user = request.user
        people1 = curr_user.sent_messages.values_list('receiver__id','receiver__picture',
                                         'receiver__username', 'receiver__first_name', 'receiver__last_name')
        people2 = curr_user.received_messages.values_list('sender__id','sender__picture','sender__username', 'sender__first_name',
                                         'sender__last_name')
        
        result_list_ = set(chain(people1, people2))
        result_list = []

        for x in result_list_:
            x = list(x)
            x[1] = request.build_absolute_uri(x[1])
            result_list.append(x)

        keys=["id","picture","username","first_name","last_name"]
        return JsonResponse([dict(zip(keys,person)) for person in result_list], safe=False)

    def check(self, request):
        curr_user = request.user
        latestMessage = curr_user.received_messages.last()
        return JsonResponse({'new':not latestMessage.seen if latestMessage else False})

    def perform_create(self, serializer):
        receiver = User.objects.filter(id=self.kwargs['user_id']).first()
        serializer.save(sender=self.request.user, receiver=receiver)
