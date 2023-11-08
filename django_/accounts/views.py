# from django.shortcuts import render
from rest_framework import viewsets,status
# from rest_framework.views import APIView
from rest_framework.response import Response
from pets.models import Adoption
from pets.serializers import AdoptionSerializer
# import requests
from djoser.views import UserViewSet


class UserAdoptionsView(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Adoption.objects.filter(user__id=self.kwargs['id'])
    serializer_class = AdoptionSerializer

# class UserActivationView(APIView):
#     def get (self, request, uid, token):
#         print('hello')
#         protocol = 'https://' if request.is_secure() else 'http://'
#         web_url = protocol + request.get_host()
#         post_url = web_url + "/auth/users/activate/"
#         post_data = {'uid': uid, 'token': token}
#         result = requests.post(post_url, data = post_data)
#         content = result.text
#         return Response(content)


 
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