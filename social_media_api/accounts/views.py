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
    