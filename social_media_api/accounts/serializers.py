from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login
from rest_framework.response import Response
User = get_user_model()

serializers.CharField(), Token.objects.create
class UserSerilalizer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','bio']


class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(write_only = True,required = True)
 
    class Meta:
        model = User
        fields = ['first_name','username','password','email']
    


    def create(self, validated_data): 
       
        validated_data.pop('email')
        user = get_user_model().objects.create_user(**validated_data)
        return user 
    



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    token = serializers.CharField(read_only=True)
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        
        # Authenticate user
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid credentials!")
        
        if not user.id:
            user.save()
        # Get or create token for the user
        token, _ = Token.objects.get_or_create(user=user)
        
        # Return relevant data
        return {
            'username': user.username,
            'email': user.email,
            'token': token.key
        }