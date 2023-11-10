from rest_framework import serializers
from .models import *

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('photo',)

class PostsSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        depth = 1

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'
        depth = 1
    
class CommentSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(many=True, read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        depth = 1

class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
        depth = 1