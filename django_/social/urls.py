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
from .views import *

urlpatterns = [
    path('', PostsView.as_view({'get': 'list', 'post':'create'}) ,name='posts'),
    path('<int:pk>', 
         PostsView.as_view({'get': 'retrieve', 'patch':'partial_update',
                             'post':'update', 'delete':'destroy'}) ,name='posts.details'),

    path('reports/', ReportsView.as_view({'get': 'list'}), name='reports'),
    path('reports/<int:pk>', ReportsView.as_view({'get': 'retrieve','delete':'destroy'}), name='reports.details'),
    path('<int:post_id>/reports/', ReportsView.as_view({'get': 'list', 'post':'create'}), name='post.report'),
    path('comment/<int:comment_id>/reports/', ReportsView.as_view({'get': 'list', 'post':'create'}), name='comment.report'),

    path('<int:post_id>/comments/', CommentsView.as_view({'get': 'list', 'post':'create'}), name='comment-list-create'),
    path('comment/<int:comment_id>/', CommentsView.as_view({'get': 'retrieve','delete':'destroy'}), name='comment-retrieve-delete'),
    path('comment/<int:comment_id>/replies/', ReplyView.as_view({'get': 'list', 'post':'create'}), name='comment-reply'),
    path('comment/replies/<int:pk>', ReplyView.as_view({'get': 'retrieve','delete':'destroy'}), name='reply.details'),
]