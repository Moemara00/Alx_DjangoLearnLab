from django.shortcuts import render
from .models import Post, Comment
from django.contrib.auth import get_user_model
from .serializers import PostSerializer, CommentSerializer
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import permissions,authentication
from rest_framework.views import APIView
from django.contrib.auth import login
from rest_framework.response import Response
User = get_user_model()

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication,
                              authentication.TokenAuthentication]
    
    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author= user)
    

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class UsersPosts(APIView):

    def get(self,request):

        followers = request.user.following.all()
        posts = Post.objects.filter(author__in= followers).order_by('created_at')

        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    
      

