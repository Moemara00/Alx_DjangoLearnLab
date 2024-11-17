from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):

    fieldsets = (None, {'fields': ('email','first_name','last_name')}),
                ('permissions', {'fields': ('is_staff', 'is_superuser')}),
                ('Personal', {'fields': ('date_of_birth', 'profile_photo')})

admin.site.register(CustomUser)
