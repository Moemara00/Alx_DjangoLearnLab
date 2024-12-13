from django.shortcuts import render
from rest_framework import generics 
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer,UserSerilalizer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class LoginView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = LoginSerializer

    
class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerilalizer
    