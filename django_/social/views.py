from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from .models import *
from .serializers import *

from rest_framework.permissions import IsAdminUser
from .permissons import UserPermission

class PostsView(viewsets.ModelViewSet):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    search_fields=['user__username', 'content']
    permission_classes = [UserPermission]
    queryset = Post.objects.all()
    serializer_class = PostsSerializer

    def perform_create(self, serializer):
        post = serializer.save(user=self.request.user)

        files = self.request.FILES.getlist('photos')
        if files:
            [Photo.objects.create(post=post,photo=f) for f in files]

    def perform_update(self,serializer):
        post = serializer.save()
        files = self.request.FILES.getlist('photos')
        if files:
            for old_photo in post.photos.all(): old_photo.delete()
            for f in files: Photo.objects.create(post=post,photo=f)

class ReportsView(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    def get_queryset(self):
        if self.kwargs.get('post_id'):
            return Report.objects.filter(post__id=self.kwargs['post_id'])
        else:
            return Report.objects.all()
    
    serializer_class = ReportsSerializer

    def perform_create(self, serializer):
        if self.kwargs.get('post_id'):
            post = Post.objects.filter(id=self.kwargs['post_id']).first()
            serializer.save(user=self.request.user, post=post)
        else:
            comment = Comment.objects.filter(id=self.kwargs['comment_id']).first()
            post=comment.post
            serializer.save(user=self.request.user, post=post, comment=comment)

class CommentsView(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data['user'] = request.user.id
        request.data['post'] = self.kwargs['post_id']
        request.data._mutable = False
        return super().create(request, *args, **kwargs)

class ReplyView(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

    def create(self, request, *args, **kwargs):
        request.data._mutable = True

        request.data['user'] = request.user.id
        request.data['comment'] = self.kwargs['comment_id']
        request.data._mutable = False

        return super().create(request, *args, **kwargs)
