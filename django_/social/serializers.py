from rest_framework import serializers
from .models import *

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('photo',)

class ReplySerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        return {
            "username": obj.user.full_name,
            "user_id": obj.user.id,
            "user_picture": obj.user.get_profile_picture(),
            "content": obj.content,
            "reply_id": obj.id,
            "created_at": obj.created_at,
        }
    class Meta:
        model = Reply
        fields = '__all__'
        optional_fields = ['user', 'comment']

class CommentSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(many=True, read_only=True)

    def to_representation(self, obj):
        data = super(CommentSerializer, self).to_representation(obj)
        return {
            "comment_id": obj.id,
            "replies": data['replies'],
            "content": obj.content,
            "created_at": obj.created_at,
            "username": obj.user.full_name,
            "user_id": obj.user.id,
            "user_picture": obj.user.get_profile_picture(),
        }

    class Meta:
        model = Comment
        fields = '__all__'
        depth = 1
        read_only_fields = ('id', 'created_at')

class ReportsSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        data = super(ReportsSerializer, self).to_representation(obj)
        data['user'] = {
            "username": obj.user.full_name,
            "user_id": obj.user.id,
            "user_picture": obj.user.get_profile_picture(),
        }
        return data
        
    class Meta:
        model = Report
        fields = '__all__'
        depth=1
        read_only_fields = ('id', 'created_at')

class PostsSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    def to_representation(self, obj):
        data = super(PostsSerializer, self).to_representation(obj)
        data['user'] = {
            "username": obj.user.full_name,
            "user_id": obj.user.id,
            "user_picture": obj.user.get_profile_picture(),
        }
        return data
    
    class Meta:
        model = Post
        fields = '__all__'
        depth = 1
        read_only_fields = ('id', 'created_at')
