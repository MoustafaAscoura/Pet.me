# from django.urls import path
# from .views import *

# urlpatterns = [
#     path('', PostsView.as_view({'get': 'hello', 'post':'create'}) ,name='posts'),
#     path('<int:pk>', 
#          PostsView.as_view({'get': 'retrieve',
#                              'post':'update', 'delete':'destroy'}) ,name='posts.details'),
    
# ]


# /posts/id/report
# /posts/id/comment
# /posts/id/comment/report
# /posts/id/reply
# -----------------------------------------------------------

from django.urls import path
from .views import (
    PostListCreateAPIView,
    PostRetrieveUpdateDeleteAPIView,
    ReportPostCreateShowAPIView,
    CommentListCreateAPIView,
    CommentRetrieveUpdateDeleteAPIView,
    ReportCommentCreateShowAPIView,
    ReplyListCreateAPIView,
    MessageListCreateAPIView,
    MessageRetrieveUpdateDeleteAPIView
)

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDeleteAPIView.as_view(), name='post-retrieve-update-delete'),
    path('posts/<int:pk>/report/', ReportPostCreateShowAPIView.as_view(), name='post-report'),
    path('posts/<int:pk>/comment/', CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('posts/<int:pk>/comment/<int:comment_id>/', CommentRetrieveUpdateDeleteAPIView.as_view(), name='comment-retrieve-update-delete'),
    path('posts/<int:pk>/comment/<int:comment_id>/report/', ReportCommentCreateShowAPIView.as_view(), name='comment-report'),
    path('posts/<int:pk>/comment/<int:comment_id>/reply/', ReplyListCreateAPIView.as_view(), name='comment-reply'),
    path('messages/', MessageListCreateAPIView.as_view(), name='message-list-create'),
    path('messages/<int:pk>/', MessageRetrieveUpdateDeleteAPIView.as_view(), name='message-retrieve-update-delete'),
]