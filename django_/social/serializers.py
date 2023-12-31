from rest_framework import serializers
from .models import *

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('photo',)

class ReplySerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        data = super(ReplySerializer, self).to_representation(obj)

        return {
            "id": obj.id,
            "username": obj.user.full_name,
            "user_id": obj.user.id,
            "user_picture": data['user']['picture'],
            "content": obj.content,
            "created_at": obj.created_at,
        }
    class Meta:
        model = Reply
        fields = '__all__'
        depth = 1
        optional_fields = ['user', 'comment']
    
    def validate(self, attrs):
        attrs['user'] = self.context['request'].user
        attrs['comment'] = Comment.objects.filter(id=self.initial_data['comment']).first()
        
        return attrs

class CommentSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(many=True, read_only=True)

    def to_representation(self, obj):
        data = super(CommentSerializer, self).to_representation(obj)
        return {
            "id": obj.id,
            "replies": data['replies'],
            "content": obj.content,
            "created_at": obj.created_at,
            "username": obj.user.full_name,
            "user_id": obj.user.id,
            "user_picture": data['user']['picture'],
        }

    class Meta:
        model = Comment
        fields = '__all__'
        depth = 1
        read_only_fields = ('id', 'created_at')
    
    def validate(self, attrs):
        post_id = self.context['request'].parser_context['kwargs']['post_id']

        attrs['user'] = self.context['request'].user
        attrs['post'] = Post.objects.filter(id=post_id).first()
        return attrs

class ReportsSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        data = super(ReportsSerializer, self).to_representation(obj)
        data['user'] = {
            "username": obj.user.full_name,
            "user_id": obj.user.id,
            "user_picture": data['user']['picture'],
        }
        return data
        
    class Meta:
        model = Report
        fields = '__all__'
        depth=1
        read_only_fields = ('id', 'created_at')

    def validate(self, attrs):
        attrs['user'] = self.context['request'].user
        
        return attrs
    
class PostsSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    def to_representation(self, obj):
        data = super(PostsSerializer, self).to_representation(obj)
        data['user'] = {
            "username": obj.user.full_name,
            "user_id": obj.user.id,
            "user_picture": data['user']['picture'],
        }
        return data
    
    class Meta:
        model = Post
        fields = '__all__'
        depth = 1
        read_only_fields = ('id', 'created_at')

    def validate(self, attrs):
        attrs['user'] = self.context['request'].user
        
        return attrs
