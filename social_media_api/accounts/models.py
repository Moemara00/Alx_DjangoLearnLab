from django.db import models
from django.contrib.auth.models import Permission, Group
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    bio = models.TextField(blank=True,null=True)
    profile_image = models.ImageField(upload_to='profile_pictures/',blank=True,null=True)
    followers = models.ManyToManyField('self',symmetrical=False,related_name='following',blank=True)


    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )