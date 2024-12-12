from django.contrib.auth import get_user_model
from rest_framework import serializers
User = get_user_model()


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
        user = User.objects.create_user(**validated_data)
        return user 
    


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required= True, write_only=True)



