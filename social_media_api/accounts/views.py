from django.shortcuts import render
from rest_framework import generics 
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer,UserSerilalizer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class LoginView(APIView):

    def post(self,request,*args,**kwargs):
        data = LoginSerializer(data=request.data)

        user = authenticate(username = data.validated_data('username'),
                            password = data.validated_data('password'))
        
        if user: 

            refresh = RefreshToken.for_user(user)
            access = refresh.access_token

            return Response({
                "refresh": refresh,
                'access': access
            })
        
        return Response({"Detail": "Wrong Credentials!"})
    

class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerilalizer
    