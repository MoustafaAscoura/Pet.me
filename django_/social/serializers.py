from rest_framework import serializers
from .models import Post,Comment, Reply, Message, Report



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





class MessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.SerializerMethodField()
    receiver_username = serializers.SerializerMethodField()

    class Meta:
        model = Message 
        fields = ['id', 'sender', 'receiver', 'content', 'created_at', 'sender_username', 'receiver_username']

    def get_sender_username(self, obj):
        return obj.sender.username

    def get_receiver_username(self, obj):
        return obj.receiver.username


    

    
class ReportsSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Report
        fields = ['id', 'user', 'post', 'created_at', 'comment', 'reason', 'username']

    def get_username(self, obj):
        return obj.user.username
