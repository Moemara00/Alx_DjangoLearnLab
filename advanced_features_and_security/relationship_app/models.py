from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, AbstractUser
 


class User_Manager(BaseUserManager):

    def create_user(self,**other_fields):

        user = self.models(**other_fields)
        user.save()
        return user 
    
    def create_super_user(self,**other_fields):

        return self.create_user(**other_fields)



class New_User(AbstractUser,PermissionsMixin):

    date_of_birth = models.DateField()
    profile_photo = models.ImageField()




 
 
 
# Define role choices
ROLE_CHOICES = (
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
)
 
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')
 
    def __str__(self):
        return f"{self.user.username} - {self.role}"
 
# Signal to create a UserProfile when a new user is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
 
# Signal to save the UserProfile when a User is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
 
 
class Author(models.Model):
    name = models.CharField(max_length=255)
 
    def __str__(self):
        return self.name
 
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=200), models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    published_date = models.DateField()
 
    class Meta:
        permissions = [
            ('can_add_book', 'Can add book'),
            ('can_change_book', 'Can edit book'),
            ('can_delete_book', 'Can delete book'),
        ]
 
    def __str__(self):
        return self.title
 
 
class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="libraries")
 
    def __str__(self):
        return self.name
 
class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="librarian")
 
    def __str__(self):
        return self.name
 