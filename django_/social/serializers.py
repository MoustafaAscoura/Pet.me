from rest_framework import serializers
from .models import Post,Report

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        #set depth = 1 for image url and user details

class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
        #set depth = 1 user details