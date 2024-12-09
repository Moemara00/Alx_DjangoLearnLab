from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm 
from django import forms
from django.contrib.auth.models import User
from .models import Post
class CustomUserCreationForm(UserCreationForm):

    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class CustomUserChangeForm(UserChangeForm):

    password = forms.CharField(required=False,widget=forms.PasswordInput,help_text='Change password or keep it')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','password')


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title','content','author']
    