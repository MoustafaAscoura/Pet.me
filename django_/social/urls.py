from django.urls import path
from .views import *

urlpatterns = [
    path('', PostsView.as_view({'get': 'list', 'post':'create'}) ,name='posts'),
    path('user/<int:user_id>/', PostsView.as_view({'get': 'list'}) ,name='user.posts'),
    path('<int:pk>/', 
         PostsView.as_view({'get': 'retrieve', 'patch':'partial_update','delete':'destroy','post':'hide'}) ,name='posts.details'),

    path('reports/', ReportsView.as_view({'get': 'list'}), name='reports'),
    path('reports/<int:pk>/', ReportsView.as_view({'delete':'destroy'}), name='reports.details'),
    path('<int:post_id>/reports/', ReportsView.as_view({'get': 'list', 'post':'create'}), name='post.report'),
    path('comment/<int:comment_id>/reports/', ReportsView.as_view({'post':'create'}), name='comment.report'),

    path('<int:post_id>/comments/', CommentsView.as_view({'post':'create'}), name='comment-create'),
    path('comment/<int:pk>/', CommentsView.as_view({'delete':'destroy'}), name='comment-delete'),
    path('comment/<int:comment_id>/replies/', ReplyView.as_view({'post':'create'}), name='comment-reply'),
    path('comment/reply/<int:pk>', ReplyView.as_view({'delete':'destroy'}), name='reply.delete'),
]