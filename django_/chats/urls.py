from django.urls import path
from .views import *

urlpatterns = [
    path('', MessagesView.as_view({'get': 'list'}), name='messages'),
    path('user/<int:receiver_id>', MessagesView.as_view({'post': 'create'}), name='message.create'),
    path('<int:pk>', MessagesView.as_view({'delete': 'destroy'}), name='message.create'),
]