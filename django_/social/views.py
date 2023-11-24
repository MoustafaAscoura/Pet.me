from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from .models import *
from .serializers import *
from .permissons import *

class PostsView(viewsets.ModelViewSet):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    search_fields=['user__username', 'content']
    permission_classes = [PostsPermission]
    serializer_class = PostsSerializer

    def get_queryset(self):
        if self.kwargs.get('user_id'):
            return Post.objects.filter(user__id = self.kwargs.get('user_id'))
        elif self.action == "list":
            return Post.objects.filter(visible=True)
        else:
            return Post.objects.all()
    
    def perform_create(self, serializer):
        post = serializer.save(user=self.request.user, visible=True)

        files = self.request.FILES.getlist('photos')
        if files:
            [Photo.objects.create(post=post,photo=f) for f in files[0:4]]

    def perform_update(self,serializer):
        post = serializer.save()
        files = self.request.FILES.getlist('photos')
        if files:
            for old_photo in post.photos.all(): old_photo.delete()
            for f in files[0:4]: Photo.objects.create(post=post,photo=f)

    def hide(self,request, pk):
        instance = self.get_object()
        instance.visible = False
        instance.save()
        return Response("Post hidden successfully", status=status.HTTP_200_OK)


class ReportsView(viewsets.ModelViewSet):
    permission_classes = [reportsPermission]
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
    permission_classes = [CommentsPermission]
    queryset=Comment.objects.all()
    serializer_class = CommentSerializer

class ReplyView(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = [CommentsPermission]

    def create(self, request, *args, **kwargs):
        request.data['comment'] = self.kwargs['comment_id']

        return super().create(request, *args, **kwargs)
