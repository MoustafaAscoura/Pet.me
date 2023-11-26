from django.urls import path
from .views import *

urlpatterns = [
    path('', MessagesView.as_view({'get':'relatedUsers'}), name='chats.users'),
    path('user/<int:user_id>/', MessagesView.as_view({'get':'list','post': 'create'}), name='message.create'),
    path('<int:pk>/', MessagesView.as_view({'delete': 'destroy'}), name='message.delete'),
    path('check/', MessagesView.as_view({'get': 'check'}), name='message.check'),
]