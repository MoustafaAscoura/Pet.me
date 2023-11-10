from rest_framework import serializers
from .models import *


class PostsSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'created_at', 'modified_at', 'content', 'user', 'username']

    def get_username(self, obj):
        return obj.user.username



class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Comment 
        fields = ['id', 'user', 'post', 'content', 'created_at', 'username']

    def get_username(self, obj):
        return obj.user.username






class ReplySerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Reply 
        fields = ['id', 'user', 'comment', 'content', 'created_at', 'username']

    def get_username(self, obj):
        return obj.user.username

    
class ReportsSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Report
        fields = ['id', 'user', 'post', 'created_at', 'comment', 'reason', 'username']

    def get_username(self, obj):
        return obj.user.username
