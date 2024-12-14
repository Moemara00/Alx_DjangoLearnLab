from rest_framework import serializers
from .models import Post, Comment



class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = [
        
                'content',

        ]

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many = True, read_only = True)
    class Meta:
        model = Post
        fields = [
                'title',
                'content',
                'comments'

        ]