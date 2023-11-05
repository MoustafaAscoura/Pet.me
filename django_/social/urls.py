from django.urls import path
from .views import *

urlpatterns = [
    path('', PostsView.as_view({'get': 'hello', 'post':'create'}) ,name='posts'),
    path('<int:pk>', 
         PostsView.as_view({'get': 'retrieve',
                             'post':'update', 'delete':'destroy'}) ,name='posts.details'),
]


# /posts/id/report
# /posts/id/comment
# /posts/id/comment/report
# /posts/id/reply
