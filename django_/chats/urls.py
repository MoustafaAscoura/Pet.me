from django.urls import path
from .views import *

urlpatterns = [
    path('user/<int:user_id>', MessagesView.as_view({'get':'list','post': 'create'}), name='message.create'),
    path('<int:pk>', MessagesView.as_view({'delete': 'destroy'}), name='message.create'),
]