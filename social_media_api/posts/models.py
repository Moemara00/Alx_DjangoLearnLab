from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content= models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
