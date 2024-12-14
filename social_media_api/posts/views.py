from django.shortcuts import render
from .models import Post, Comment
from django.contrib.auth import get_user_model
from .serializers import PostSerializer, CommentSerializer
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import permissions,authentication
User = get_user_model()

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]
    search_fields = ['title']
    
    def perform_create(self, serializer):
       serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)