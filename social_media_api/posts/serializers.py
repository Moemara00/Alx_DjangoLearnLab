from rest_framework import serializers
from .models import Post, Comment



class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = [
                'post',
                'content',


        ]

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only = True)
    author = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Post
        fields = [
                'id',
                'title',
                'content',
                'comments',
                'author',

        ]
    def get_author(self,obj):
        return obj.author.username
    




'''
make a relationship between posts and comments 




'''