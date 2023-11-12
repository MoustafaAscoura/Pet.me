import requests

from rest_framework import viewsets,status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.permissions import IsAuthenticated



from djoser.views import UserViewSet

from .models import User
from .serializers import UserSerializer
from pets.models import Adoption
from pets.serializers import AdoptionSerializer


class SocialAuthCompleteView(APIView):
    def get(self, request, provider):
        code, state = str(request.GET['code']), str(request.GET['state'])
        json_obj = {'code': code, 'state': state}

        return Response(json_obj)

class UserListView(generics.ListCreateAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    search_fields=['username', 'first_name', 'last_name']

#Activate user email
class ActivateUser(UserViewSet):
    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
 
        kwargs['data'] = {"uid": self.kwargs['uid'], "token": self.kwargs['token']}
        return serializer_class(*args, **kwargs)
 
    def activation(self, request, uid, token, *args, **kwargs):
        super().activation(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)