from django.shortcuts import render
from rest_framework import generics 
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer,UserSerilalizer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from django.contrib.auth import get_user_model, login
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework import permissions
from .models import CustomUser
CustomUser.objects.all()
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):

        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors)
      


class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):

            serializer = LoginSerializer(data = request.data)
            if serializer.is_valid():
                 return Response(serializer.validated_data)
            return Response(serializer.errors)
    
class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerilalizer
    







class FollowView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, id):
        """
        Handle user follow action.
        """
        try:
            user_to_follow = User.objects.get(id=id)
        except User.DoesNotExist: 
            raise NotFound(detail="User not found", code=status.HTTP_404_NOT_FOUND)

       
        if request.user == user_to_follow:
            return Response(
                {"detail": "You can't follow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )

    
        if user_to_follow in request.user.following.all():
            return Response(
                {"detail": "You are already following this user!"},
                status=status.HTTP_400_BAD_REQUEST
            )

        
        request.user.following.add(user_to_follow)
        return Response(
            {"detail": f"Started following {user_to_follow.username}."},
            status=status.HTTP_201_CREATED
        )



class UnFollowView(generics.GenericAPIView):
     permission_classes = [permissions.IsAuthenticated]
     def get(self,request,id):
          
        try:
               user_to_unfollow = User.objects.get(id=id)
            
        except User.DoesNotExist:
             
                raise NotFound(detail="User is not found",code=status.HTTP_404_NOT_FOUND)
        
        if request.user == user_to_unfollow:
             
             return Response({'details': "You can't unfollow yourself"},
                             status=status.HTTP_400_BAD_REQUEST)
        
        if user_to_unfollow not in request.user.following.all():
             return Response({"detail": "You are already not following this user"},
                             status=status.HTTP_400_BAD_REQUEST)
        

        request.user.following.remove(user_to_unfollow)
        return Response({"detail": f"Now You Are Not Following {user_to_unfollow}"})