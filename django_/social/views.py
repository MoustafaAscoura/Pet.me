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