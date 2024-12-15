from django.shortcuts import render
from .models import Post, Comment,Like
from notifications.models import Notification
from django.contrib.auth import get_user_model
from .serializers import PostSerializer, CommentSerializer
from rest_framework import viewsets
from rest_framework import filters,status
from rest_framework import permissions,authentication,generics
from rest_framework.views import APIView
from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
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

        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('created_at')
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    
      

class LikingView(generics.GenericAPIView):

    permission_classes = [permissions.IsAuthenticated]
    def get(self,request,pk):

        post_to_like = get_object_or_404(Post,pk=pk)

        if Like.objects.filter(user=request.user,post=post_to_like).exists():
            return Response({"detail": 'You are already Liked it'},status=status.HTTP_400_BAD_REQUEST)
        
        Like.objects.create(user=request.user,post=post_to_like)

        if request.user != post_to_like.author:
            
            Notification.objects.create(
                actor = request.user,
                recipient = post_to_like.author,
                verb = "Liked your post",
                target = post_to_like,

            )

        # generics.get_object_or_404(Post, pk=pk) Like.objects.get_or_create(user=request.user, post=post)

        return Response({'detail':'You now liked it'},status=status.HTTP_201_CREATED)
    
        


class UnLikingView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,pk):

        post_to_unfollow = get_object_or_404(Post,pk=pk)

        liked_post = Like.objects.filter(post=post_to_unfollow,user=request.user).first()

        if not liked_post:
            return Response({"detail":'You did not like this post'})


        liked_post.delete()
        return Response({'detail':'You dislike the post successfully'},status=status.HTTP_201_CREATED)
    


