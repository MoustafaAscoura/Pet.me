import requests

from rest_framework import viewsets,status
from rest_framework.views import APIView
from rest_framework.response import Response
from djoser.views import UserViewSet
from django.urls import reverse


from pets.models import Adoption
from pets.serializers import AdoptionSerializer


class UserAdoptionsView(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Adoption.objects.filter(user__id=self.kwargs['id'])
    serializer_class = AdoptionSerializer

class SocialAuthCompleteView(APIView):
    permission_classes = []

    def get(self, request, provider):
        code, state = str(request.GET['code']), str(request.GET['state'])
        json_obj = {'code': code, 'state': state}

        return Response(json_obj)
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = web_url + f"/accounts/auth/o/{provider}/"


        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        result = requests.post(post_url, data = json_obj,headers=headers)
        return Response(result.json())


#Activate user email
class ActivateUser(UserViewSet):
    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
 
        # this line is the only change from the base implementation.
        kwargs['data'] = {"uid": self.kwargs['uid'], "token": self.kwargs['token']}
 
        return serializer_class(*args, **kwargs)
 
    def activation(self, request, uid, token, *args, **kwargs):
        super().activation(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)