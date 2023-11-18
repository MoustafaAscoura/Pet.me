from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.permissions import IsAdminUser

from djoser.views import UserViewSet

from .models import User
from .permissons import UserPermission
from .serializers import UserSerializer

class UserListView(generics.ListAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    search_fields=['username', 'first_name', 'last_name']

class UserSingleView(generics.RetrieveDestroyAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]
