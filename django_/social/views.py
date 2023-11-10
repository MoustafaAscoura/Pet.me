# from rest_framework import viewsets
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.parsers import JSONParser 
# from rest_framework.renderers import JSONRenderer

# from django.http.response import HttpResponse

# from .models import Post
# from .serializers import PostsSerializer


# # Create your views here.
# class PostsView(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostsSerializer


# def report_post(request,id):
#     request.
#     data = JSONParser().parse(request)
#     serializer = PostsSerializer(data=data) 

#     if serializer.is_valid(): 
#         serializer.save()
#         jdata = JSONRenderer().render(res)
#         return HttpResponse(jdata, content_type='application/json')
        
#     return Response(serializer.errors, status=400) 

# --------------------------------------------------------------------------

from rest_framework import generics
from .models import *
from .serializers import *


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer

class PostRetreiveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer


# ---- report ----


class ReportPostCreateShowAPIView(generics.CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportsSerializer


# -- comment --


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# report a comment
class ReportCommentCreateShowAPIView(generics.CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportsSerializer


# ----reply----
class ReplyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReplySerializer
    
