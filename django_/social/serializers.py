from rest_framework import serializers
from .models import Post,Comment, Reply, Message, Report

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        #set depth = 1 for image url and user details



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment 
        fields = '__all__'


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply 
        fields = '__all__'


    
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message 
        fields = '__all__'


    

class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
        #set depth = 1 user details


