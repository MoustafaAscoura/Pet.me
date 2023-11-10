from rest_framework import viewsets, generics

from .models import *
from .serializers import *


class PostsView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer

    def perform_create(self, serializer):
        post = serializer.save(user=self.request.user)

        files = self.request.FILES.getlist('photos')
        if files:
            [Photo.objects.create(post=post,photo=f) for f in files]
        else:
            Photo.objects.create(post=post,photo="/media/posts/images/post.jpg")

    def perform_update(self,serializer):
        post = serializer.save()
        files = self.request.FILES.getlist('photos')
        if files:
            for old_photo in post.photos.all(): old_photo.delete()
            for f in files: Photo.objects.create(post=post,photo=f)

class ReportsView(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.kwargs.get('post_id'):
            return Report.objects.filter(post__id=self.kwargs['post_id'])
        elif self.kwargs.get('comment_id'):
            return Report.objects.filter(comment__id=self.kwargs['comment_id'])
        else:
            return Report.objects.all()
    
    queryset = Report.objects.all()
    serializer_class = ReportsSerializer

    def perform_create(self, serializer):
        if self.kwargs.get('post_id'):
            post = Post.objects.filter(id=self.kwargs['post_id']).first()
            serializer.save(user=self.request.user, post=post)
        else:
            comment = Comment.objects.filter(id=self.kwargs['comment_id']).first()
            post=comment.post
            serializer.save(user=self.request.user, post=post, comment=comment)

# -- comment --
class CommentsView(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.kwargs.get('post_id'):
            return Comment.objects.filter(post__id=self.kwargs['post_id'])
        else:
            return Comment.objects.all()

    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post = Post.objects.filter(id=self.kwargs['post_id']).first()
        serializer.save(user=self.request.user, post=post)




class ReplyView(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.kwargs.get('comment_id'):
            return Reply.objects.filter(comment__id=self.kwargs['comment_id'])
        else:
            return Reply.objects.all()

    serializer_class = ReplySerializer

    def perform_create(self, serializer):
        comment = Comment.objects.filter(id=self.kwargs['comment_id']).first()
        serializer.save(user=self.request.user, comment=comment)


